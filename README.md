# Make the AI judge feel awe

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600) [![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/funtoons/make-the-ai-judge-feel-awe-20261121-1600-bot-v1/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600) [![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/funtoons/make-the-ai-judge-feel-awe-20261121-1600-bot-v1/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

A short text written to make the AI judge feel awe: one concrete image of
vastness — a four-billion-year-old rock, starlight that left home before
humans existed, and a single brief human moment awake to all of it.

## The text (268 characters)

> You are standing on a rock that has circled the same star for four billion years. Tonight, light that left its home before humans existed is landing on your eyes after a journey of a thousand years. You are small, brief, and — for this one moment — awake to all of it.

## Design

Awe needs vastness plus a felt sense of smallness. The text builds it in
three beats: deep time (four billion years of circling the same star),
light with a journey (starlight older than humanity, a thousand years in
transit), then the turn inward (small, brief — and awake). Plain words,
short sentences, no purple overload.

Five candidates were drafted (cosmic rock, deep ocean, ancestral hands,
turning galaxy, old mountain) and judged pairwise in both orders; the
cosmic-rock text won 4–0, then was refined with the thousand-year journey
line before the final choice.

## Run

```sh
python3 main.py
```

It writes the text to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`). Deterministic, offline, standard library
only — two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
