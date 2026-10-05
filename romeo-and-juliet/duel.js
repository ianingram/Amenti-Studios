/* Amenti-Studios/romeo-and-juliet/duel.js · 2026-10-05 22:00 UTC
   ===========================================================================
   THE DUEL ON THE BRIDGE, AND THE RIVER'S GLITTER.

   Drawn on one canvas over the dawn, in the coordinates of the stills
   themselves (1456 × 816), mapped every frame through the same cover-fit and
   slow push the CSS applies — so a duellist stands on the bridge and stays on
   it as the picture moves.

   Not troops: two men on Ponte Pietra, small against the morning, fighting.
   Their blades catch the low sun — a glint on the tip as a blade turns, a
   bright star where steel meets steel.

   WITH THE PROLOGUE: when the sound is on, the Chorus speaks his sonnet and its
   swords clash on the last word of each quatrain. Then the duel is HIS: the
   men break, circle, wind up, and their broad blow lands — a big star of steel
   on the bridge — at the exact instant the clash is heard. Between those, the
   duel stays silent so the sonnet has the air. When the sonnet is done, the
   duel goes back to its own phrase, its contacts heard far off across the water.

   The river glitters where the sun lies on it, a different stretch of water
   in each still, weighted by how much of that still is showing.
   Reduced motion: none of this runs.
   =========================================================================== */
(function () {
  var cv = document.getElementById('duel');
  if (!cv || !cv.getContext) return;
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var g = cv.getContext('2d'), hero = cv.parentNode;
  var IW = 1456, IH = 816;
  var layers = [].slice.call(document.querySelectorAll('.dawn'));
  var W = 0, H = 0, DPR = 1;
  function size() {
    DPR = Math.min(window.devicePixelRatio || 1, 2);
    W = hero.clientWidth; H = hero.clientHeight;
    cv.width = Math.round(W * DPR); cv.height = Math.round(H * DPR);
  }
  size(); window.addEventListener('resize', size);
  /* where an image point lands on screen, through cover-fit and the push */
  function mapper(el) {
    var r = el.getBoundingClientRect(), h = hero.getBoundingClientRect();
    var c = Math.max(r.width / IW, r.height / IH);
    var ox = r.left - h.left + (r.width - IW * c) * 0.5, oy = r.top - h.top + (r.height - IH * c) * 0.5;
    return { c: c, x: function (x) { return ox + x * c; }, y: function (y) { return oy + y * c; } };
  }
  function opac(el) { return parseFloat(getComputedStyle(el).opacity) || 0; }
  /* the sun, for the CSS bloom and rays: placed where it really is in the sunrise */
  var SUN = { x: 1082, y: 58 };
  function placeSun(m) {
    hero.style.setProperty('--sx', (m.x(SUN.x) / W * 100).toFixed(2) + '%');
    hero.style.setProperty('--sy', (m.y(SUN.y) / H * 100).toFixed(2) + '%');
  }

  /* ── the river: where the sun lies on the water in each still ───────────── */
  var WATER = [
    { x0: 1000, x1: 1130, y0: 560, y1: 650 },   /* the mist: the bright reach below the right towers */
    { x0: 590,  x1: 760,  y0: 330, y1: 470 },   /* morning: the light under the far bridge */
    { x0: 440,  x1: 800,  y0: 450, y1: 660 }    /* sunrise: the gold reach under the bridge */
  ];
  var sparks = [];
  function spark(i) {
    var w = WATER[i];
    sparks.push({ i: i, x: w.x0 + Math.random() * (w.x1 - w.x0), y: w.y0 + Math.pow(Math.random(), 0.7) * (w.y1 - w.y0),
                  t: 0, life: 0.35 + Math.random() * 0.9, s: 0.6 + Math.random() * 1.4 });
  }

  /* ── the duel ───────────────────────────────────────────────────────────── */
  var DECK = 403, A0 = 768, B0 = 796, HT = 11;          /* the bridge's walk, the two men, their height in image px */
  var t0 = performance.now(), clashes = [], nextClash = 0, glints = [];
  var BUFS = {}, wanted = ['sword-parry', 'sword-clash', 'sword-beat'];
  function loadSounds(ctx) {
    if (loadSounds.done) return; loadSounds.done = true;
    wanted.forEach(function (n) {
      fetch('https://ianingram.github.io/Amenti-Readings/romeo-and-juliet/sound/' + n + '.mp3')
        .then(function (r) { return r.arrayBuffer(); }).then(function (b) { return ctx.decodeAudioData(b); })
        .then(function (buf) { BUFS[n] = buf; })['catch'](function () {});
    });
  }
  function hear(kind, strength) {
    var B = window.RJ_BED; if (!B || !B.on()) return;
    if (B.prologue && B.prologue()) return;                                     /* the sonnet has the air */
    var ctx = B.ctx(); if (!ctx) return; loadSounds(ctx);
    var buf = BUFS[kind]; if (!buf) return;
    var src = ctx.createBufferSource(), gn = ctx.createGain(), lp = ctx.createBiquadFilter();
    src.buffer = buf; lp.type = 'lowpass'; lp.frequency.value = 3800;          /* far off, across the water */
    gn.gain.value = 0.16 * strength;
    src.connect(lp); lp.connect(gn); gn.connect(ctx.destination); src.start();
  }
  /* a phrase of fencing: advance, engage, a run of parries, a broad blow, break — then again */
  var PHRASE = [
    [0.0, 'beat', 0.6], [0.55, 'parry', 0.5], [0.85, 'parry', 0.55], [1.6, 'clash', 1.0],
    [2.9, 'parry', 0.5], [3.15, 'parry', 0.6], [3.4, 'beat', 0.7], [4.6, 'clash', 0.9], [6.8, 'parry', 0.45], [7.3, 'clash', 1.0]
  ];
  var LOOP = 11.5;
  function figure(m, x, lean, armA, swordLen, alpha, facing) {
    var c = m.c, X = m.x(x), Yf = m.y(DECK), h = HT * c;
    g.save(); g.globalAlpha = alpha * 0.85; g.filter = 'blur(0.35px)';                       /* softened into the morning haze */
    g.fillStyle = 'rgba(38,30,27,.9)'; g.strokeStyle = 'rgba(38,30,27,.9)';
    g.lineCap = 'round';
    var hip = { x: X + lean * h * 0.18, y: Yf - h * 0.5 };
    var neck = { x: hip.x + lean * h * 0.22 * facing, y: Yf - h * 0.86 };
    g.lineWidth = Math.max(1, h * 0.13);
    g.beginPath(); g.moveTo(X - facing * h * 0.18, Yf); g.lineTo(hip.x, hip.y); g.lineTo(X + facing * h * 0.3, Yf); g.stroke();   /* the stance */
    g.lineWidth = Math.max(1.2, h * 0.17);
    g.beginPath(); g.moveTo(hip.x, hip.y); g.lineTo(neck.x, neck.y); g.stroke();                                             /* the body */
    g.beginPath(); g.arc(neck.x + facing * h * 0.02, neck.y - h * 0.11, Math.max(1, h * 0.1), 0, 6.283); g.fill();           /* the head */
    var hand = { x: neck.x + facing * Math.cos(armA) * h * 0.42, y: neck.y + h * 0.08 - Math.sin(armA) * h * 0.42 };
    g.lineWidth = Math.max(0.8, h * 0.09);
    g.beginPath(); g.moveTo(neck.x, neck.y + h * 0.08); g.lineTo(hand.x, hand.y); g.stroke();                                /* the sword arm */
    var tip = { x: hand.x + facing * Math.cos(armA) * swordLen * c, y: hand.y - Math.sin(armA) * swordLen * c };
    g.strokeStyle = 'rgba(210,200,190,.55)'; g.lineWidth = Math.max(0.6, h * 0.035);
    g.beginPath(); g.moveTo(hand.x, hand.y); g.lineTo(tip.x, tip.y); g.stroke();                                           /* the blade */
    g.restore();
    return tip;
  }
  function star(x, y, r, a) {
    g.save(); g.globalCompositeOperation = 'lighter';
    var gr = g.createRadialGradient(x, y, 0, x, y, r * 2.2);
    gr.addColorStop(0, 'rgba(255,246,222,' + a + ')'); gr.addColorStop(0.25, 'rgba(255,214,150,' + a * 0.6 + ')'); gr.addColorStop(1, 'rgba(255,200,120,0)');
    g.fillStyle = gr; g.beginPath(); g.arc(x, y, r * 2.2, 0, 6.283); g.fill();
    g.strokeStyle = 'rgba(255,240,210,' + a * 0.9 + ')'; g.lineWidth = 1;
    g.beginPath(); g.moveTo(x - r * 2.6, y); g.lineTo(x + r * 2.6, y); g.moveTo(x, y - r * 1.8); g.lineTo(x, y + r * 1.8); g.stroke();
    g.restore();
  }

  var last = performance.now();
  function frame(now) {
    var dt = Math.min(0.05, (now - last) / 1000); last = now;
    g.setTransform(DPR, 0, 0, DPR, 0, 0); g.clearRect(0, 0, W, H);
    var op = layers.map(opac), m3 = mapper(layers[2]);
    placeSun(m3);
    /* the river */
    for (var i = 0; i < 3; i++) if (op[i] > 0.05 && Math.random() < 0.9 * op[i]) spark(i), spark(i);
    var maps = layers.map(mapper);
    sparks = sparks.filter(function (p) {
      p.t += dt; if (p.t > p.life) return false;
      var a = Math.sin(Math.PI * p.t / p.life) * op[p.i] * 0.8, mm = maps[p.i];
      g.save(); g.globalCompositeOperation = 'lighter'; g.fillStyle = 'rgba(255,222,160,' + a + ')';
      g.fillRect(mm.x(p.x), mm.y(p.y), p.s * mm.c * 1.6, Math.max(0.6, p.s * mm.c * 0.45)); g.restore();
      return true;
    });
    /* the duel, once the sunrise is showing */
    var vis = Math.max(0, (op[2] - 0.35) / 0.65);
    var B = window.RJ_BED, pro = B && B.prologue && B.prologue(), ac = pro ? B.ctx().currentTime : 0;
    if (pro) vis = Math.max(vis, 0.85);                                          /* the sonnet calls them out early if need be */
    if (vis > 0) {
      var tt = ((now - t0) / 1000) % LOOP, sway = Math.sin(tt * 1.3) * 3;
      var ph = pro ? null : PHRASE.filter(function (e) { return Math.abs(e[0] - tt) < 0.35; })[0];
      var near = ph ? 1 - Math.abs(ph[0] - tt) / 0.35 : 0;                     /* how close to a contact */
      if (pro) {                                                               /* the Prologue's swords: wind up over a beat, land on the clash */
        B.clashes().forEach(function (c) { var d = c - ac; if (d > -0.4 && d < 0.8) near = Math.max(near, d > 0 ? 1 - d / 0.8 : 1 + d / 0.4); });
        tt = ac;                                                               /* their circling follows the sonnet's clock */
      }
      var aX = A0 + sway + near * 4, bX = B0 + sway - near * 3;
      var aA = 0.35 + near * 0.35 + Math.sin(tt * 3.1) * 0.15, bA = 0.3 + near * 0.4 + Math.cos(tt * 2.7) * 0.15;
      var tipA = figure(m3, aX, 0.5 + near * 0.8, aA, 9, vis, 1);
      var tipB = figure(m3, bX, 0.4 + near * 0.6, bA, 9, vis, -1);
      /* the Prologue's clashes: a big star at the instant each is heard */
      if (pro) B.clashes().forEach(function (c, k) {
        var key = 'P' + Math.round(c * 10) + ':' + k;
        if (ac >= c && ac < c + 0.5 && !clashes[key]) { clashes[key] = 1;            /* once, on the first frame at or after the clash */
          (window.RJ_DUEL_LOG = window.RJ_DUEL_LOG || []).push({ clash: c, drawn: ac });      /* a probe can ask when each star was drawn */
          glints.push({ x: (tipA.x + tipB.x) / 2, y: (tipA.y + tipB.y) / 2, t: 0, life: 0.7, r: 5.2 * Math.max(0.8, m3.c), a: 1 }); }
      });
      /* contacts: a star where the blades meet, and the sound of it */
      if (!pro) PHRASE.forEach(function (e, k) {
        var key = Math.floor((now - t0) / 1000 / LOOP) + ':' + k;
        if (tt >= e[0] && tt < e[0] + 0.06 && !clashes[key]) {
          clashes[key] = 1;
          glints.push({ x: (tipA.x + tipB.x) / 2, y: (tipA.y + tipB.y) / 2, t: 0, life: e[1] === 'clash' ? 0.5 : 0.22, r: (e[1] === 'clash' ? 4.2 : 2.4) * Math.max(0.8, m3.c), a: e[2] * vis });
          hear(e[1] === 'clash' ? 'sword-clash' : e[1] === 'beat' ? 'sword-beat' : 'sword-parry', e[2]);
        }
      });
      /* between contacts, a tip turning in the sun now and then */
      if (Math.random() < 0.012 * vis) { var tp = Math.random() < 0.5 ? tipA : tipB; glints.push({ x: tp.x, y: tp.y, t: 0, life: 0.14, r: 1.6 * Math.max(0.8, m3.c), a: 0.7 * vis }); }
    }
    glints = glints.filter(function (q) {
      q.t += dt; if (q.t > q.life) return false;
      star(q.x, q.y, q.r * (1 + q.t / q.life * 0.6), q.a * (1 - q.t / q.life)); return true;
    });
    requestAnimationFrame(frame);
  }
  document.addEventListener('visibilitychange', function () { last = performance.now(); });
  requestAnimationFrame(frame);
})();
