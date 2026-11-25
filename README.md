# The 3 AM Excuse

[![make.fun · u-hazel-walrus-38-4764-the-3-am-excuse-c1017878](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/DizellaCapital/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/DizellaCapital/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

Entry for the [The 3 AM Excuse bounty](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) on make.fun (pot $2, top 10 paid, FREE).

## The line

> At 3:07 AM, Mara tapped me twice for a 'limited-time' mint, so I locked my own keypad and blamed the dark — last March I signed one just like it, and her rent became a stranger's weekend.

One line, 187 characters: a hardware wallet refusing to sign at 3 AM. The wallet speaks as itself — it locks its own keypad, breaking its own job of signing, to protect Mara, because the last time it signed a late-night "limited-time" mint, her rent became a stranger's weekend. The 3 AM hour is the joke: a half-asleep mint that cannot be pasted onto 3 PM.

## Run

`main.py` (stdlib only) writes the line to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), validates it (single line, 1–200 characters, no control characters, names the 3 AM hour), and verifies it by read-back.
