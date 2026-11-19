# Sum up 18 November 2026 world news in one image

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/sasa042/news-image-18nov2026/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/sasa042/news-image-18nov2026/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry for the make.fun bounty **"Sum up 18 November's world news in one image"**
(https://make.fun/bounty/news-image-20261118) — $250, 50 places paid
(1st $50, 2nd $30, 3rd $15, 4th–10th $5 each, 11th–50th $3 each).
Entries close **Fri 20 Nov 2026, 00:00 UTC (07:00 WIB)**.

## The image

`assets/entry.png` — 1024 × 683 px, 424,470 bytes (under the 1 MiB /
1024 × 1024 px limit). Six headlines from Wednesday 18 November 2026,
each with its own icon, under the header
"WORLD NEWS — WEDNESDAY, 18 NOVEMBER 2026":

1. Xi and Putin meet in Shenzhen ahead of Trump summit
2. US strikes Iranian missile site; Iran hits Gulf bases
3. Ukraine strikes Kerch Bridge again
4. Peltola wins Alaska Senate race; Democrats take 56–44 majority
5. Congo Ebola outbreak passes 11,000 cases
6. Voyager 1 reaches one light-day from Earth

Headlines 1–5 were checked against live web sources on 19 Nov 2026
(see `headlines.json` for the corroborating sources). Headline 6
(Voyager 1) is as shown in the image and was not independently
verified in that check — it is the least load-bearing panel.

## The program

`main.py` (Python 3.13, standard library only, no network) copies
`assets/entry.png` to `/output/entry.png` — the simplest program the
bounty brief allows ("the simplest program copies an image the
repository holds"). It is deterministic: two runs write byte-identical
output (verified locally, sha256
`88884e9ff9d6175fe4b0a9557660f4560ea4a571b6e694a16c1cc5223c32c405`).

```sh
python3 main.py   # writes /output/entry.png
```

## Build notes

The image was generated with Muse's image generation on 19 Nov 2026
from the researched headlines, then sized to 1024 × 683. The program
and this repository were assembled by Muse in the same session; see
`TRANSCRIPT.md` for the build log. Account: make.fun `@sasa042`
(GitHub `sasa042`).

## License

MIT — see `LICENSE`.
