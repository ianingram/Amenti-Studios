# Amenti Studios

Front of house. The productions as the public meets them.

    index.html              the lobby — the bill of productions
    dracula/index.html      the Dracula production front
    dracula/dracula-hero.jpg

---

## Two repos, and the line is audience

| | |
|---|---|
| **[Amenti-Readings](https://github.com/ianingram/Amenti-Readings)** | the workshop — cue sheets, the cast, chapter maps, the player, the cutting tool |
| **Amenti-Studios** | this. The lobby and the production fronts. |

Nobody visiting a theatre needs `cut.js`.

The split was made at one production rather than three, because moving a lobby
is cheap and moving an established address is not.

**The audio is in neither repo.** It renders to R2, keyed by
`TTS_MODEL + voice + style + text`, so there is no artefact to file.

---

## Adding a production

A production is a folder. Add the folder, add a row to `PRODUCTIONS` in
`index.html`, and that is the whole operation — there is no build step and no
index to regenerate.

The voice count and the scripted-chapter count on each bill are read **live**
from the workshop's `cast.json` and `<work>/index.json`, so a recast or a new
episode cannot leave this page stale. When the workshop is unreachable the
bills still draw, without the counts: a lobby that empties itself because a
fetch failed is worse than one that is merely less specific.

---

Ingram Manor LLC · 2026 · All Rights Reserved

The texts are public domain. The productions are not.
