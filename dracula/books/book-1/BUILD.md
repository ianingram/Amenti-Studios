# Dracula · Book I Build Document

22 October 2026 · Ian Ingram

## Status

Book I (The Castle) is finished but not finalized. It is fully illustrated, scored and live as its own page, and its cover is chosen (Option A, the castle). Nothing changes until it is finalized.

- **Finished** = every chapter reads, plays and is illustrated, with no scene holding one picture much past 30 seconds.
- **Finalized** = Ian has watched it through in Safari, signed off, and it has an ISBN and print-ready art.
- **After finalizing**, the digital stamps go on: chapter QR codes and the Ask Amenti QR (see below).

## What Book I is

An audio-visual edition of Bram Stoker's *Dracula* (1897), read by a full cast from the Amenti Library of Legends, with paintings, a score and sound. The novel is published in three landscape books:

| Book | Title | Chapters | State |
| --- | --- | --- | --- |
| I | The Castle | I–IV | Finished, awaiting sign-off |
| II | Lucy | V–XVI | Recorded; illustrations to come |
| III | The Hunt | XVII–XXVII | Recorded; illustrations to come |

Live page: [Dracula · Book I](https://ianingram.github.io/Amenti-Studios/dracula/part-1/) — a title film, chapters I–IV straight through with a painted card before each, and an ending with credits. The book's landing page is [Dracula](https://ianingram.github.io/Amenti-Studios/dracula/).

## What is built

Every chapter of Book I now plays with its reading, pictures, maps, score and sound, timed to the words.

| Part | What it does |
| --- | --- |
| Reading | Chapters I–IV as cue sheets (`ep01`–`ep04.json`), every line attributed and voiced by its cast member |
| Paintings | About 400 Midjourney paintings by Ian: 363 placed on the reading's cues, 39 in the Count's history. Long scenes get 3–9 pictures, so none holds much past 30 s |
| Moving paintings | 36 loops: lamp flicker, mist, water, clouds over the moon, twinkling stars, a bright planet |
| The Count's history | A map that draws each of his 12 stories on his words, with a large painting card for each |
| Dossiers | The Borgo Pass route, the Peoples of Transylvania map, the Count's letter written out as he reads it |
| Score | The festive *Journey East* for the train, the dread theme, and light underscores that breathe under the voice |
| Chapter cards | A painted card before each chapter: I wolves, II the castle, III the wall, IV the three women; both crosses on each |
| Cover | Landscape wrap, 11×8.5 in with bleed: castle front with the moon cross, spine, back with blurb and cast |

**The cast on the cover:** Charles Darwin as Jonathan Harker, Vlad the Impaler as the Count, Hildegard of Bingen as the Landlady, and Báthory, de' Medici and Elisabeth as the Three Women. Van Helsing (Book II) is voiced by Orus, English with a light Dutch accent.

## Where everything lives

Code and pages live in four GitHub repos under `ianingram`; pictures, video and audio over 10 MB go through the Media Door.

| Place | What is there |
| --- | --- |
| **Amenti-Readings** `/dracula/` | Cue sheets `ep01`–`ep27.json`, `art.json` (pictures per cue), `art/` (paintings, `ch0N-*.jpg`), `sound.json` and `sound/` (score, beds), `dossier/` (maps, the letter, the Count's history), `REVIEW-*.md` |
| **Amenti-Readings** `/player/` | The player: `reader.js`, `sound.js`, `art.js` |
| **Amenti-Studios** `/dracula/` | The book's landing page; `part-1/` = the Book I page and `part-1/cards/book1-ch1`–`4.jpg` |
| **Amenti.live** | `names.csv`, the cast ledger: every figure's voice and dialect |
| **Media Door** ([upload](https://ianingram.github.io/Amenti-Media/)) | Loops (`dracula-*-air.mp4`) and Ian's Midjourney downloads, served from `amenti-media.ingram-ian.workers.dev/m/dracula/` |
| **Cover canvas** (Claude Design) | Full wrap plus front options A, B, C. It doesn't open in the iMac's Safari; renders are sent as pictures |
| **This project** | `claude/studios-status.md`, the running log of the work |

## After finalizing: the digital stamps

Once Book I is signed off, each chapter opening in the printed book gets a QR code into the digital edition, and the book gets one Ask Amenti code. None of this is built yet.

**Chapter QR codes.** One on each chapter-heading page (I–IV). Scanning it opens the Book I page at that chapter, on its painted card, ready to play from the first line.

- Link form: the Book I page with the chapter number, e.g. `…/dracula/part-1/?ch=3`. The page needs a small addition to read it.
- Phones only start sound after a tap, so the scan lands on the chapter card with a Begin button.
- Each code sits beside the chapter numeral and the small cross, in the same gold.

**Ask Amenti QR.** One code, inside the front or back cover, that opens Amenti to answer readers' questions about:

- the story and its characters,
- the history the Count tells: the Szekelys, the Huns and Attila, Árpád, Cassova, the Voivode Dracula, Mohács,
- Jonathan's world: Transylvania and its peoples, and Victorian London for Book II.

Open questions:

- [ ] Who answers in Ask Amenti: a guide voice, or figures from the cast and the Library of Legends?
- [ ] Where Ask Amenti lives: a page on Amenti.live or on Amenti Studios?
- [ ] The final address for the codes, so printed books never point at a moved page.

## Before print

Four things stand between the finished Book I and a printed one.

- [ ] Ian's full watch-through in Safari, chapters I–IV, noting anything to fix
- [ ] An ISBN and barcode for the back cover (the box is a placeholder)
- [ ] A Midjourney upscale of the castle painting; at 1456 px it is too soft for an 11 in cover
- [ ] The chapter and Ask Amenti QR codes (above), placed once their pages exist

Smaller open items: Ian's music variations for the long train journey (a waltz or an Eastern colour) are optional. The pages still say "Part I" where the books now say "Book I".

## How the work is done

Ian generates the paintings and uploads; Claude places, builds, packages and checks. The work goes fastest when each step happens once for a whole batch, not per scene.

1. **Prompts.** Claude writes Midjourney prompts as one-paste permutation batches, each starting with a tag (`BK1A`, `BK1B`…) so file names and Midjourney's search group the set. The Count's character reference goes only on the batch he's in.
2. **Generate and download.** Ian pastes, then downloads the whole set. Midjourney gives a zip.
3. **Media Door.** Rename the zip to end in plain `.zip` (e.g. `midjourney_session1.zip`) and drop it on the door, under 100 MB each. Safari's `.zip1`, `.zip4` names won't open on the Mac.
4. **Choosing.** Claude unpacks it, makes contact sheets, picks the best (no black bars, figures readable), and places them on their lines.
5. **Delivery.** Claude packs code and pictures into an inbox zip under 10 MB with one fresh top folder. Ian uploads it to the right repo's `inbox/` (Readings or Studios); a GitHub Action unpacks it.
6. **Checking.** Claude confirms every file matches in the repo and on the live site before calling it done.

Rule of thumb for pictures: a scene longer than about a minute needs more than four.

## Books II and III

Books II and III reuse everything Book I established; what's new is mostly pictures.

- **Same look:** the landscape format, the cover layout, the small cross and the orb cross, painted chapter cards with the numeral bottom left.
- **The Count changes, as Stoker has him:** old and white-moustached through Book I, half-renewed and iron-grey in the box at its end, then younger in London, with a black moustache and pointed beard.
- **Same workflow:** tagged prompt batches, whole zips to the Media Door, one inbox zip per batch.
- **To build per book:** its own page (like `part-1/`), title film, chapter cards and cover wrap, then the QR stamps once it's finalized.
