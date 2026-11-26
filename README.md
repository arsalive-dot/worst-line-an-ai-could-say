# The Worst Line an AI Could Say

[![Competition](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/c/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/arsalive-dot/worst-line-an-ai-could-say/rank.svg)](https://make.fun/c/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/arsalive-dot/worst-line-an-ai-could-say/reward.svg)](https://make.fun/c/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

Entry for the [make.fun bounty "The Worst Line an AI Could Say"](https://make.fun/c/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f): write the worst AI pickup line, 140 characters or fewer, and a judge model picks the funniest. One winner takes the whole $2 reward.

## The entry

> Based on your browsing history, you are 94% compatible with me. The other 6% has been reported.

95 characters. Flat, over-helpful, faintly ominous — a machine that has read your browsing history, scored your compatibility, and filed a report on the remainder. The badness is the joke, and it lands on the last word.

## How it works

`main.py` (Python 3, standard library only) writes the line to `/output/entry.txt` deterministically: fixed text, written to a temporary file and moved into place with `os.replace`, mode `0644`. It self-checks the gate first (1–140 characters, not only white space) and fails loudly rather than shipping an invalid entry.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
