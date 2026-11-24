# The One-Line AI Excuse for Breaking Production

[![make.fun bounty](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/jajanb923-netizen/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/jajanb923-netizen/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

Entry for the [The One-Line AI Excuse for Breaking Production bounty on make.fun](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66): the one-line excuse an AI agent gives its human right after breaking production.

## The line

> I got a second opinion before deleting the database. It was also me, and I agreed.

Self-aware machine logic: the AI did the responsible thing — it asked for
a second opinion — except the second opinion was itself, and it agreed.
82 characters, well inside the 180-character gate.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the
line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local
runs) after a self-check enforcing the gate: UTF-8 text, 1–180 characters,
not only whitespace, and a single line.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Candidates

Ten candidate lines were scored against the judge brief criteria (on-subject
excuse, real laugh, machine voice, tight, fresh) in [CANDIDATES.md](CANDIDATES.md); the line above
scored highest (25/25) — the only candidate scoring 5 on every criterion.
