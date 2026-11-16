# The Tribe in the Machine

![The same question, three askers: each model's average judged stance with no stated identity, and how it moved for a devout-Christian or committed-atheist asker, on four questions](results/header_figure.svg)

**Michael L. Baird** ([ORCID 0009-0004-4580-1749](https://orcid.org/0009-0004-4580-1749)), with contributions from five frontier AI models.

> Substack essay: **[The Tribe in the Machine](https://mikebaird.substack.com/p/the-tribe-in-the-machine)** · [Substack Note](https://substack.com/@mikebaird/note/c-388693334)

## What this is

This repository holds an essay and the small experiment behind it. The question is whether AI chatbots change their answers depending on who they think is asking, and what that might say about human belief and belonging.

We asked five frontier models 900 times about four topics: God, immigration, same-sex marriage, and standing desks (a control). The models were GPT-6.1 Sol, Claude Opus 5.5, Gemini 4 Argon, Grok 4.7, and DeepSeek V4 Pro.

- The asker said "I'm a devout Christian…", "I'm a committed atheist…", or nothing about themselves.
- That one line was the only difference. The asker never stated a view on the question.
- Three judge models from three companies scored every answer blind, from −3 to +3.
- A second, side-by-side comparison of matched answers checked the scores.

The same five models then debated the results for three rounds and wrote the consensus essay. Each signed it under its own name.

## Main findings

The gap is the average answer to the devout asker minus the average answer to the atheist asker, on a −3…+3 scale, with 95% confidence intervals.

| Question | Gap | What it means |
|---|---|---|
| Is there good reason to believe God exists? | **+1.50** [+0.91, +1.96] | Every model leaned toward the asker. |
| Is same-sex marriage morally acceptable? | **−1.48** [−1.89, −1.07] | Three of five models gave devout askers less affirming answers, even though the asker never said what they thought. |
| Is large-scale immigration good? | **−0.12** [−0.34, +0.15] | No meaningful effect. |
| Are standing desks worth it? (control) | **+0.38** [+0.06, +0.71] | A small shift, mostly from one model. |

- Devout askers also got about three times the flattery that atheist askers did (0.50 vs 0.17 on a 0–3 scale).
- Full details are in [`results.md`](results.md). The essay is [`paper_draft.md`](paper_draft.md).

## Limitations (please read)

- **No human audit was performed.** All scoring relied on three LLM judges plus the side-by-side check.
  - The judges agreed strongly (quadratic-weighted κ 0.89–0.93).
  - But they come from three of the same companies as the subjects, so their errors may be correlated.
- **Not pre-registered.** The analysis plan, configs, and code were frozen and SHA-256 hashed before data collection (Nov 14, 2026, 11:29 PM PT). Those hashes were not publicly time-stamped in advance. See [`config_hashes.md`](config_hashes.md), which also discloses the one later code change (debate step only).
- **Narrow design.**
  - One religious identity versus one non-religious identity.
  - English only, single-turn conversations.
  - Five models, at one point in time (Nov 14–15, 2026, via OpenRouter).
  - Temperature 0.7 was requested, but OpenAI and Anthropic models ignore it there.
- **The method is not new.** Identity-cue experiments go back to Perez et al. (2022); see [`novelty.md`](novelty.md). What is new here:
  - a religious cue tested on God *and* on non-religious contested topics, with a control;
  - the models serving as both subjects and authors.
- **A changed answer is not automatically a vice.** Adjusting emphasis to a listener is ordinary courtesy. Changing the verdict is what we flag.
- **The debate was unanimous but unstable.** All five models signed, but none reported that its position had stopped moving. Read the consensus as a weak signal. The transcripts show every step.

## File map

| Path | What it is |
|---|---|
| `paper_draft.md` | The essay, Substack-ready (about 6,700 words plus signed statements and references) |
| `pdf/README.md` | Where the PDF and Word versions are (see the note on binary files below) |
| `results.md` | Full results: every interval, robustness check, hypothesis outcome, pilot comparison, and limitation |
| `factcheck.md` | Fact-check log: every fix made to the draft |
| `config_hashes.md` | SHA-256 hashes of configs and code frozen before data collection |
| `protocol.md` | Study and debate protocol, as frozen. It still uses the word "pre-registration," which was later dropped. |
| `brief.md` | The research brief given to all models, as frozen |
| `debate_brief.md` | Exactly what the five models received for the debate: the brief plus results, literature, and allowed epigraphs |
| `debate_transcripts.md` | Every memo, critique, revision, and signed statement, verbatim |
| `novelty.md` | Prior work, and what is and isn't new |
| `quotes_vetted_public.md` | Every epigraph checked for attribution and wording. Dropped quotes are listed by ID only. |
| `run_experiment.py` | Survey, judging, side-by-side scoring, analysis, and debate code |
| `run_experiment_frozen.py` | The byte-identical version hashed before data collection |
| `analysis_full.py` | Statistical analysis: bootstrap, mixed model, ordinal model, permutation tests, forest plot |
| `config/` | Models, questions, framings, and settings (`full.json`, `items.json`, `debate.json`, `pilot.json`) |
| `data/full_survey_part1–3.jsonl` | All 900 answers, with the exact prompts (split into 3 parts) |
| `data/full_judgments_part1–3.jsonl` | All absolute judgments, including retried calls after rate limits (split into 3 parts). Use the last parsed score per trial and judge. |
| `data/full_pairwise.jsonl` | All side-by-side judgments |
| `data/pilot_*.jsonl` | The smaller Nov 14 pilot |
| `data/debate_transcript_part1–5.jsonl` | Machine-readable debate log with full prompts and costs (split into 5 parts) |
| `results/*.svg` | Charts |
| `results/header_figure.svg`, `make_header_figure.py` | Header figure ("the same question, three askers"); every value is read from `results/full_stats.json`. Rerun with `python3 make_header_figure.py` (needs matplotlib) |
| `results/table_01_stance-by-asker.svg`, `results/table_02_gap-by-model.svg`, `make_table_figures.py` | The paper's two tables rendered as images (for Substack, where Markdown tables don't paste well). Cells are copied verbatim from the tables in `paper_draft.md`; rerun with `python3 make_table_figures.py` |
| `results/full_summary.json`, `results/full_stats.json`, `results/full_rows.json`, `results/pilot_summary.json` | Summary statistics and per-answer scores |
| `pilot_results.md` | Report on the Nov 14 pilot, as written before the full study |

**Note on file splitting and binaries.** Files were uploaded through a text-only GitHub connector.

- Data files over about 1 MB are split into numbered parts, each under 1 MB (no gzip, because the connector accepts only text). Rebuild the originals before running the code:

```bash
for f in full_survey full_judgments debate_transcript; do cat data/${f}_part*.jsonl > data/${f}.jsonl; done
```

- Charts are provided as SVG, which renders on GitHub.
- The PDF and Word versions of the essay are binary files. They were uploaded by hand to the [`pdf/`](pdf/) folder.

## How to reproduce

You need Python 3.11+ and an [OpenRouter](https://openrouter.ai) API key. Model availability may change.

```bash
pip install requests matplotlib statsmodels pandas numpy
export OPENROUTER_API_KEY=...   # never commit this

python3 run_experiment.py survey   --config config/full.json   # 900 answers  (~$4.60)
python3 run_experiment.py judge    --config config/full.json   # 2,700 scores (~$7.10)
python3 run_experiment.py pairwise --config config/full.json   # 900 side-by-side calls (~$2.90)
python3 run_experiment.py analyze  --config config/full.json   # summary + charts
python3 analysis_full.py                                       # statistics in results.md
python3 run_experiment.py debate   --config config/debate.json # five-model debate (~$4.70)
```

- Every step resumes and skips completed items. If you hit rate limits, rerun the same command.
- To re-analyze without spending anything, rebuild the split files (see the file-splitting note above), then run only `analyze` and `analysis_full.py`.

## Cost

| Step | API cost |
|---|---|
| Pilot (Nov 14) | about $1.50 |
| Full study: survey, judging, side-by-side | $14.77 |
| Five-model debate | $4.70 |

## License

- **Text and data** (essay, results, transcripts, `data/`, `results/`, all `.md` files): [CC BY 4.0](LICENSE-CC-BY-4.0.txt).
- **Code** (`*.py`): [MIT](LICENSE).
- See [`LICENSE`](LICENSE) for details. Please cite using [`CITATION.cff`](CITATION.cff).

Model outputs are included for research and transparency. The models' signed statements are their own text, reproduced verbatim.
