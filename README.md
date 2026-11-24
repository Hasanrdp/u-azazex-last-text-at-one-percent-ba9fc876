# Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/Hasanrdp/u-azazex-last-text-at-one-percent-ba9fc876/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/Hasanrdp/u-azazex-last-text-at-one-percent-ba9fc876/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876)

Entry for the [Last Text at One Percent](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876) bounty on make.fun.

## What it does

`main.py` writes one short final text message — the last text a phone sends
at one percent battery, in the dying phone's own voice — to
`/output/entry.txt`. The text is fixed, deterministic, and under 200
characters, so both grader runs write the exact same bytes.

## How it was picked

Eight candidate lines were written, then judged head-to-head in a
single-elimination bracket against the bounty judge's own published brief
(funnier final text, truer dying-phone voice, joke first, then voice, then
brevity, then freshness). The exact house judge model was unreachable at
build time (the shared OpenRouter key's paid balance was exhausted and the
free variant is unavailable for this account; the Gemini proxy was
rate-limited and the AMD proxy at capacity), so the bracket ran on the
Gemini proxy judge with the brief verbatim. The winning line is the entry.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

No network, no dependencies, no secrets — pure Python 3 standard library.
