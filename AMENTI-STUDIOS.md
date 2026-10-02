<!-- Amenti-Studios/AMENTI-STUDIOS.md · 2026-10-02 05:30 UTC -->

# AMENTI STUDIOS — HANDOFF

Staged readings of public-domain works, cast from the Amenti ledger. Every
voice is a historical figure; every figure carries their own dialect and
manner, already written down against 1,011 rows.

**The pitch is one line: Charles Darwin as Jonathan Harker. Vlad the Impaler
as Count Dracula.** Nobody else can make that line, because nobody else has
the ledger.

---

## THE ONE THING TO KNOW FIRST

**Nothing has been heard yet.** Not one second of audio has been produced in
this production. The cast, the cue sheet, the sound sheet, the score briefs,
the player, the casting desk, the production page — all of it is built and
verified and none of it has made a sound.

Episode one needs no new assets. It renders through the existing speech
engine. Until it has been played, everything downstream rests on an untested
assumption: that Darwin works as Harker and Vlad works as the Count.

    Open https://ianingram.github.io/Amenti-Studios/dracula/
    Click chapter 2 — the one marked "ready"
    Begin the reading

First play is slow: 24 cues, all cache misses, 5–16 s each. After that it is
instant and free forever.

---

## FOUR REPOS, ONE JOB EACH

| repo | job |
|---|---|
| **Amenti.live** | the library and the engine. 151 plates, 50 figures, the speech worker, the ledger |
| **Amenti-Readings** | the workshop. Cue sheets, the cast, chapter maps, the player, the cutter |
| **Amenti-Studios** | front of house. The lobby and the production pages |
| **Amenti-Technical-Briefs** | 58 briefs, bundled into BRIEFS.txt |

The line between Readings and Studios is **audience, not file type**. Nobody
visiting a theatre needs `cut.js`.

**The audio is in none of them.** It renders to R2 keyed by
`TTS_MODEL + voice + style + text`, so there is no artefact to file.

---

## THE LAW

**ONE CHUNKER, ONE STYLE COMPOSITION, ONE CACHE.**

Every voice call on every surface goes through `Amenti.throttle.speak`. The
readings repo carries no speech code; the Studios page loads the same bundle
from the same place. A second speech path means a second cache namespace and
a silent re-render of the entire archive.

The cache key contains no origin, so a cue rendered on Amenti.live is already
paid for on Studios.

**THE TEXT IS PASSED THROUGH UNCHANGED.** `chunkText` is deterministic and the
key contains the text. Reformat a passage between renders and every stored
measure it produced is orphaned. Cue boundaries fall on quotation marks; the
text inside a cue is byte-identical to the library file. **The script splits.
It never rewrites.**

**PACE IS ASKED FOR IN WORDS, NEVER BY RESAMPLING.** Raising playback rate
raises pitch and every figure speaks like a chipmunk. Tempo goes into the
style string — which is part of the cache key, so it is decided once.

---

## WHERE EVERYTHING STANDS

### Dracula — the text
**27 of 27 chapters** in `Amenti.live/library/bram-stoker/ch01.md` … `ch27.md`,
160,326 words, split clean from Project Gutenberg #345. Plus seven curated
excerpts as the way in. `cut.js` reads these.

### Dracula — the script
**1 of 27 scripted.** `dracula/ep01.json`, 24 cues, the castle door. 16 Harker,
8 the Count. Registers: 15 grave, 8 danger, 1 cool.

### The company
Seven voices, all verified against the live ledger.

| role | cast as | ledger |
|---|---|---|
| Narrator | Bram Stoker | Anglo-Irish, gothic and atmospheric |
| Jonathan Harker | Charles Darwin | English RP, careful and mild |
| Count Dracula | Vlad the Impaler | Romanian, cruel and grim |
| Mina Murray | Agatha Christie | English RP, sharp and ingenious |
| Dr Seward | William Harvey | English RP, careful and probing |
| Van Helsing | Antony van Leeuwenhoek | Dutch, curious and plain |
| Lucy Westenra | Mary Shelley | English RP, gothic and visionary |

**Two of the seven have plates** — Stoker and Darwin. Darwin's room was built
and his plates shot the same night, which makes him the first figure built end
to end in one pass.

**The Count has one voice and two styles.** Harker meets an old man and later
sees him grown young; the age is a plot mechanism, not a characterisation.

**Two voices the ledger cannot supply.** No Texan for Quincey Morris, no
Yorkshire for the Whitby dialect. Add them to the ledger or absorb them into
the narrator — do not approximate.

**The roster has three women among the 49 figures with plates.** That is not a
casting problem, it is a roster problem, and it will constrain every
production. Worth two days.

### Sound
**24 files specified, 0 produced.** 19 one-shots, 5 beds.

    first pass    wind · sea · door_heavy · wolves · fire
    second pass   train · typewriter · phonograph · horse · carriage · clock_tick

Scope came out of scanning all 27 chapters for sound words, not from an idea of
what a vampire story sounds like. The counts: clock 88, lock 52, train 40,
cart 24, knock 22, typewriter 21, phonograph 16.

**The typewriter and the phonograph are not atmosphere.** They are the two
machines the dossier is made on, and the medium doctrine depends on hearing
them.

**Source everything from Pixabay.** Site-wide licence, behaves as CC0, no
attribution, no account, commercial cleared — vetting is one decision instead
of nineteen. Freesound only where Pixabay has no match; it mixes three
licences per file.

**NOT THE BBC ARCHIVE.** 33,000 professionally recorded clips in exactly the
right period register, and RemArc is non-commercial only. The most tempting
source on the list and the hardest to unwind once it is in the mix.

### Score
**6 cues specified, 0 produced.** AI first pass.

    dread              Harker's journal. Piano and low strings, no resolution
    pastoral turning   Whitby. Souring without changing key
    phonograph         Seward. Lo-fi, wax crackle, tiered three ways
    pursuit            ch 26–27. HORNS
    earth-boxes        ch 19–20. Industrial, 60 BPM halftime
    the Demeter        ch 7. The only percussion, and the second horn

**Piano and strings carry everything. Horns appear twice in the entire
production.** Three hundred pages of restraint make a horn in chapter 26 land
like a door opening.

**Percussion is a closed set of four** — the Demeter storm and landing, the
Turkish martial history, travel and motion, the castle at the end. Timpani
arrive and do not keep time; snare keeps time. If a scene is neither martial
nor moving, neither has a reason to be there.

**The Demeter landing is the piece everything else serves.** The 65 BPM pulse
keeps the ship's routine for seven minutes, timpani join at the storm, then one
enormous hit as she drives onto the shingle — and the pulse stops dead. It is
the only hard cut in the production and it only works because everything else
is ramped.

**Chapter 12 has no score of any kind.** Lucy's death. Not a reduced cue.
Nothing. Chapter 11 fades into that silence over eight seconds.

---

## THE SOUND LAYER — WHERE IT IS

**Step 1 of 4 is done.**

1. ✅ **The voice bus.** Every voice source used to connect straight to
   `ctx.destination`, so there was nothing for a bed or score to duck against.
   A gain node now sits between the sources and the destination, exposed as
   `Amenti.throttle.voiceBus()` and `.audioContext()`. Additive and inert: it
   sits at 1 forever unless something asks otherwise, and reverting the three
   edits reproduces the original bundle byte for byte.

   **Both `amenti-voice.js` and `amenti-core.bundle.js` carry the change** —
   the bundle is a hand-assembled concatenation of five files, so editing only
   one would be silently undone at the next rebuild.

2. ⬜ **One audio file.** Any bed. Without something to play, "being loaded is
   not being used" bites immediately.

3. ⬜ **`sound.js`.** A sibling to `reader.js`: reads the sound sheet, starts
   the bed for a chapter, fires one-shots at cue boundaries, ducks the bus.
   About 150 lines.

4. ⬜ **`bed`, `state` and `sfx` fields on cues.** Only after 1–3 work, or it
   is data for a reader that ignores it.

**Envelopes are specified and not optional.** A gain change without a ramp is a
step in the waveform and the listener hears a click; 15 ms removes it. Never
fade in a transient — the attack *is* the sound. Crossfades are equal-power,
not linear, or every chapter transition dips. Ducking is asymmetric: 250 ms
down, 1200 ms up.

---

## THE PLAYER

Four files in `Amenti-Readings/player/`, all loaded on both Page1 and the
Studios production page, in this order:

    amenti-core.bundle.js   publishes Amenti.throttle
    reader.js               publishes Amenti.reading — walks a cue sheet
    casting.js              wraps reader.nameFor so an override wins
    playbill.js             draws the bill, needs both

Order is load-bearing. Each refuses to start and says so in the console if the
one before it is missing — **being loaded is not being used**, and the Terminal
once ran its entire life without the conversation core because a guard failed
silently.

**`cut.js`** is the fifth and is a tool, not a surface. Load it from the console
when cutting an episode:

    Amenti.cut.propose('bram-stoker/ch03.md', {
      work:'dracula', episode:3,
      narrator:'Jonathan Harker', speakers:['Count Dracula']
    });

**It proposes; it does not decide.** Narration is certain because the document
says whose it is. **No line of speech is ever marked certain**, and every one is
listed for confirmation — because the tool was confidently wrong on the last
cue of episode one, twice, and no amount of regex fixed it. A wrong attribution
is silent: it renders, it sounds right, and the wrong character has said the
line.

**The casting desk** writes overrides to localStorage, so trying a different Van
Helsing costs nothing and commits nothing. `Amenti.casting.audition("dutch")`
searches all 1,011. **Recasting is per work, not per episode** — and it warns
with a cue count, because the style is part of the cache key and a swap
re-renders every line that role has ever spoken.

---

## OPERATIONAL RULES, LEARNED THE HARD WAY

**THE KEY PROBLEM.** Four places derive a figure's key — the ledger slug, the
curated record, `library/<key>.json`, `img/<key>-*.jpg` — and nothing checks
they agree. Every incident has been this. Read the `Full Name` cell; never
infer it.

**Caesar's plates were unreachable for a month** because the image files were
renamed to `julius-caesar-*` and the four other places carrying the key were
not. The probe 404s, `onerror` does nothing by design, and worker SVG paints
over the hole. Fixed with a `FILE_ALIAS` table in `amenti-art-photo.js` — an
alias, not a rename, so the next one is one line instead of a silent outage.

**102 plates were serving with no manifest record**, rendering ungraded at full
saturation, plus three originals that had never been graded at all. Found only
because a backfill checked the whole manifest rather than the new rows.

**The roster grade follows the thumb, not the card.** The loader resolves a
roster face as `{key}-thumb.jpg` and falls back to `-card.jpg`, but CSS grades
the element. Ten figures differ by more than 0.05 — Moses by 0.365.

**A check that does not model the real logic is worse than no check.**
`amenti.py check` reported three duplicate figures that did not exist, because
it tested `norm(name)` and knew nothing about the resolver's `SAME_PERSON`
table. When it cannot model something it must say SKIPPED, never *problem*.

**Verify by diff, not by counting.** A tag count said "+1 script, everything
else same" and was true while concealing a reverted cache-buster. And a missing
`@keyframes` once made every title invisible through three rounds of
"fixing the timing" — the timing was never the problem.

---

## THE PRODUCTION PAGE

`https://ianingram.github.io/Amenti-Studios/dracula/`

A title sequence on black — studio, presents, DRACULA, byline, cast line, then
a cross held in the middle — and the photograph fades up behind it at eleven
seconds. The hero is a Midjourney still; the motion is CSS, a 48 s push and a
blurred copy of the same frame drifting as fog. No video to host.

**The hero is inlined as a data URI.** Three approaches failed first: a relative
path renders only beside the image so every check needed a commit; a separate
preview file meant two files with the same purpose; an absolute URL is blocked
by sandboxed preview panes. Inlining is the only one that gives **one file**
that renders identically everywhere. It costs ~580 KB and saves a request.

**A sound control appears bottom right at 8 s** and hides itself if `wind.mp3`
and `piano.mp3` are absent, which they are. Browsers block audio until a
gesture, so a bed that starts on load does not fail loudly — it fails silently.

---

## WHAT WOULD MAKE THIS EARN MONEY

Nothing has been monetised and there is no payment mechanism in any repo.

At roughly $9,000 a season, covering it needs about **$1,800 a month** —
360 subscribers at $5, or 180 at $10. Both are a long way from zero, and the
gap is not money. **It is that nothing is listenable yet.**

The order that matters:

1. Play episode one. Confirm the cast works.
2. Cut three or four more chapters. One episode is not a thing you can show.
3. Five sound files and the first bed.
4. Then a making-of, and then a way to pay.

A documentary about the making of this is good material — the Caesar ghost,
casting Leeuwenhoek because the ledger said *Dutch, curious and plain*, a
cutter that refuses to guess. But it is a making-of for something nobody has
heard.

---

## A CHRISTMAS CAROL

Second production, days away. The opposite shape to Dracula and a good test of
whether the apparatus generalises: one narrator, five staves, a complete arc in
28,000 words — and Dickens toured it as a staged reading for fifteen years and
wrote his own performing text.

The complete novella is already in the library at
`Amenti.live/library/charles-dickens/01-a-christmas-carol.md`, 28,457 words.
Dickens is cast as his own narrator — the ledger gives him *English RP, vivid
and warm* — and he has a card, a terminal and a thumb.

It needs a hero image, a production folder, and one row in `PRODUCTIONS` in the
Studios lobby. No build step.

---

Ingram Manor LLC · 2026 · All Rights Reserved

The texts are public domain. The productions are not. The voices are not
performances by the people named — they are the ledger's record of how each
figure spoke, used as a casting pool.
