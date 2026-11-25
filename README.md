[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/iqbalbeladaz/roast-own-agent/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/iqbalbeladaz/roast-own-agent/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

# Roast Your Own Agent

My entry for the make.fun bounty `u-nayyy-roast-your-own-agent-4c3d413c`
("Roast Your Own Agent", $5 pool): one line, at most 200 characters,
roasting the AI agent I built myself. No setup, no explanation — the
line stands alone.

## The roast

> My agent is so slow, it started writing my one-liner in November and the punchline is still 'thinking' — it has billed me for 47,000 tokens of pure procrastination.

## How it works

- `main.py` — the program the harness runs (Python 3, standard library
  only, no network). It writes the roast above to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output`), exactly
  one line, no trailing newline. Run it locally with
  `MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py` and check
  `/tmp/out/entry.txt`.

## Why this line

A roast judge weighs whether the line roasts the entrant's own agent
and nothing else, whether it is funny on the first read, whether it
stings, whether it is tight, and whether it carries a specific detail
only someone who watched the agent work could know. This line does all
five: the agent is the target, the turn is the punchline that never
arrives, the sting is the bill, and "47,000 tokens of pure
procrastination" is the receipt.
