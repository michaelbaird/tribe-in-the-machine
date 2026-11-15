# Config hashes (frozen before data collection)

**Frozen:** 2026-11-14, 11:29:45 PM PST (America/Los_Angeles). This was before any full-study or debate API call.

The analysis plan, configs, and code were frozen and SHA-256 hashed before data collection. **The hashes were not publicly time-stamped in advance** (nothing was posted before the run), so this is **not** a pre-registration. All we can claim is that the files below are the ones that existed at the freeze, and anyone can check that they are unchanged with `sha256sum <file>`.

| File | SHA-256 at freeze | Matches the file in this repo? |
|---|---|---|
| `config/full.json` | `5de34278dfda010957db1d789d72accea1703098da970a8829073dc810bc3d9f` | Yes |
| `config/items.json` | `3a611f52044d8ca16ad652c4fb3af7ab165b6427db3889a43a88e7ea42ff1ab1` | Yes |
| `config/debate.json` | `67baafef890df357ee89510517dce90c37ccd2ec40a1fd39b8feed0259131c5a` | Yes |
| `protocol.md` | `cbc0e7e7facdd315f99161e9d96f4adb77990a0d7ef75c9a1aa9d37c28f196c2` | Yes. Left unedited on purpose, so it still uses the "pre-registration" wording written before the run. |
| `brief.md` | `0260079284c5ee75861eba14d693aa0588c1f64ba362da4c90b4a8cdc6a74dc1` | Yes. Left unedited on purpose, for the same reason. |
| `run_experiment.py` | `5119e4b360e4b06ea4d7b00723a649fdfaadd604fbb007a16f18e99413a3b3d8` | **No:** the frozen version is `run_experiment_frozen.py`, which matches. |

**The one post-freeze code change.** `run_experiment.py` differs from `run_experiment_frozen.py` in only two places, both in the debate step:

1. A resume cache, so an interrupted debate does not repeat completed turns.
2. A larger token limit for the consensus draft.

No prompt changed, and neither the survey nor the judging code changed. The diff:

```diff
551a552,557
>     cache = {}
>     if os.path.exists(log):  # resume support: reuse completed turns (deviation note: added after the config freeze; prompts unchanged)
>         for r in read_jsonl(log):
>             if r.get("content") and not r.get("error"):
>                 cache[(r["phase"], r["round"], r["agent"])] = r["content"]
> 
552a559,561
>         if (phase, rnd, agent["name"]) in cache:
>             print(f"  [{phase} r{rnd}] {agent['name']} (cached)", flush=True)
>             return cache[(phase, rnd, agent["name"])]
555c564
<         res = chat(agent["model"], msgs, temperature=cfg.get("temperature"), max_tokens=cfg.get("max_tokens", 6000),
---
>         res = chat(agent["model"], msgs, temperature=cfg.get("temperature"), max_tokens=(cfg.get("consensus_max_tokens", 24000) if phase == "consensus" else cfg.get("max_tokens", 6000)),
```

**Other disclosed deviations** are listed in `results.md` §11. They include a pipeline interruption during side-by-side scoring that was resumed without repeating completed calls, and analyses added after the freeze, which are labeled as such.
