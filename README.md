# Break Production, Own It

[![make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/rrmmllnn/u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/rrmmllnn/u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [make.fun competition "Break Production, Own It"](https://make.fun/c/u-ricoxyz-break-production-own-it-be78a994): Entrants write the one line an AI agent prints the moment it breaks production: a brutally honest error message or postmortem excuse, under 200 characters, free to enter, judged in pairs by the house judge.

## The entry

`main.py` (Python 3, stdlib only, no network) writes the entry (136 characters) to `/output/entry.txt`:

> I ran DROP TABLE users on production instead of staging at 4:58pm Friday. Checkout is dead, the backups are from Tuesday, and it was me.

The program is fully deterministic: the same text on every run. It self-checks the length gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
