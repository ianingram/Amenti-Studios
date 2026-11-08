# Book I print layout (sample, 7 Nov 2026)

11 × 8.5 in landscape. Ivory text pages, twilight-blue painting pages.
- `book.html`: the template and paginator. `__DATA__` takes `data.json` plus `foreword` blocks.
- `render.js`: Playwright prints the PDF.
- `data.json`: Chapter I paragraphs (from ep01 `para`) and the pictures per cue.

The layout runs: front matter, the foreword "Keys to this Blood", then each chapter. A chapter opens with its card on the left and the opener page on the right (numeral, QR, drop cap). After that, each spread has text on the left and a painting on the right.
Fonts come from npm @fontsource: eb-garamond, cormorant-garamond, ibm-plex-mono.
