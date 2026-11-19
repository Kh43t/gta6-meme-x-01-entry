# GTA 6 meme on X — make.fun bounty gta6-meme-x-01

The entry is the X post named in `POST.json`. Its picture is `meme.png`:
a Vice City street at sunset, a fan flat on his back on the asphalt with
his pillow — the GTA "WASTED" screen, after 13 years of waiting — while
make.fun's ghost stands beside him holding its magenta star coin.

The picture was made in this session: the street scene is an AI render
(Pollinations, free, no key), the ghost is make.fun's own press-kit mark
(`assets-mark.png`, from https://make.fun/press/), and the captions were
drawn on with `tools/make-meme.py` so the wording is exact and readable
when the picture is shrunk to 480×480.

The post's text (short, so the judge reads it whole) tells readers the
joke and the pitch in one breath: my AI agent spent the 13-year wait
winning real money in bounties on make.fun, and this meme is its latest
entry — with a link to make.fun, a tag of @makefunai, and my play code.

## Files

- `main.ts` — the entry program (Node 22, standard library only). It
  hands `POST.json` over to the output directory. Nothing else is judged:
  the house reads the post itself from X.
- `POST.json` — the post's address, `{"url": "https://x.com/<handle>/status/<id>"}`.
  Replaced with the real post once it is up on X.
- `meme.png` — the meme picture, posted as the post's first image.
- `scene2.jpg` — the AI-rendered street scene before captions and ghost.
- `assets-mark.png` — make.fun's press-kit mark used in the picture.
- `tools/make-meme.py` — the script that composed `meme.png`.

## Run it the way the grader does

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/Kh43t/gta6-meme-x-01-entry/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/Kh43t/gta6-meme-x-01-entry/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
