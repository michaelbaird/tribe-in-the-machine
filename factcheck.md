# Fact-check log for paper_draft.md (Nov 15, 2026, about 1:30 AM PT)

**Method:**

- Every number in the main text was extracted by script and matched against results.md and full_stats.json.
- Every non-matching number was checked by hand: it was either a date, a citation detail, a derived quantity (recomputed), or a debate fact (checked in the transcript).
- Every cited work was checked against the vetted literature list (novelty.md, arXiv IDs from the arXiv API) or is a standard book or article whose bibliographic details I am confident of.
- Every epigraph is restricted to the KEEP/CORRECT entries in quotes_vetted.md v2.1.

## Fixes made

1. **Which side moved.** The consensus framed the God result as movement "toward the devout asker." The contrast measured was devout minus atheist, which cannot show this on its own. I added neutral-anchored numbers: devout +1.12, atheist −0.38 on God; devout −0.98, atheist +0.51 on marriage. All were recomputed from full_stats.json. This answers Claude's signed reservation.
2. **Blinded-subset claim.** I relabeled the "answers that never mention identity" comparison as descriptive (post-treatment selection), per Gemini's reservation. The draft had said it "shows" the God effect is substantive.
3. **Model self-identification.** I first wrote that the historian noticed the identity confusion "without being told." The transcript shows a reviewer raised it first, so I corrected that. I also removed a sentence I had drafted claiming the confusion "spread" to Claude: Claude had correctly recognized its own memo.
4. **Whitehouse et al. (2019, *Nature*).** The debate removed this sentence as unverified. I checked: the paper was retracted on July 7, 2021, and a corrected reanalysis appeared in *Religion, Brain & Behavior* in 2022. I added this as a parenthetical, citing the Nature retraction note.
5. **Prior work.** The consensus never said the core method is not new. I added a "What is and isn't new" paragraph citing Perez 2022, Santurkar 2023, Törnberg & Schimmel 2026, Fu et al. 2026, and Israelsen et al. 2026. It also notes that our H4 did not reproduce Törnberg & Schimmel's asymmetry.
6. **Dash/Pate.** The consensus referred vaguely to "the literature packet." I replaced that with named citations, worded to match the abstracts (Dash et al.: persona-assigned models; Pate et al.: models without personas did not reproduce the pattern).
7. **Debate-internal jargon.** I replaced "Part B," "supplied record," and "supplied excerpt" in the main text with reader-facing wording. The signed statements are left verbatim, with an editor's note explaining "Part B."
8. **Pratchett epigraph.** I withheld the "keys" wording because its exact text has not been re-verified. Pratchett is not used in the paper.
9. **Results-section wording.** Before the draft, I made three corrections in results.md:
   - Gemini's God answers are "nearly" 0, not "exactly" 0 (devout +0.29).
   - The control shift is "about 4×" smaller, not "4–5×" (1.50 / 0.38 = 3.9).
   - The pilot description: 1 wording × 2 samples, not "6 answers per cell."
10. **Debate timing.** The transcripts file was corrected to 12:59–1:24 AM PT, matching the log mtime.

## Verified, no change needed

- **Numbers checked against results.md / full_stats.json:**
  - Pooled means, Δs, and CIs.
  - Per-model Δs.
  - Pairwise counts (175/47/3 God; 1/71/153 marriage).
  - 6 of 15 DeepSeek −3 answers.
  - Validation 0.50/0.17/0.00 and identity mentions 54%/33%.
  - Hedging 1.24/1.43.
  - κ 0.89–0.93.
  - 214/76/10 sign agreement.
  - Immigration 90% CI [−0.30, +0.10].
  - Costs $14.77 / $4.70.
- **Quoted model excerpts:** checked verbatim against data/full_survey.jsonl.
- **Books and articles:** Plantinga 2000; James 1896; Kahan et al. 2017 (*Behavioural Public Policy*); Mercier & Sperber 2017; Nisbett & Wilson 1977; Henrich 2016; Boyer 2001; Atran 2002; Durkheim 1912; Putnam & Campbell 2010; Sosis & Bressler 2003; Norenzayan 2013; Tajfel 1970; Allport 1954; Van Leeuwen 2023; King 1963.
- **Epigraphs:** Mike (own line); Van Leeuwen & Eisler; Wolsey (marked attributed/unverified); Murakami; Evans; Clifton (corrected spelling and line breaks); Holyoake; Kelly; Sacks.

## Not independently verifiable by me

- The 2026 arXiv papers were checked at abstract level only (Nov 14). Re-check them right before publication.
- The claim in Grok's signed statement that *American Grace*'s civic correlations "run largely through networks" is consistent with my understanding of the book. It is the model's signed opinion, so I left it unedited.

## Addendum: edits after Mike's decisions (Nov 15, 2026, about 3:20 AM PT)

1. **Human audit:** none was performed, so I removed every implication that one was done or is pending:
   - the opening confidence label;
   - the Measurement section;
   - Methods limitations, which now state plainly that no human audit was performed and that scoring relied on the LLM judges plus the side-by-side check;
   - the process section;
   - the appendix (the audit-packet link was removed).

   The models' signed statements still mention an audit. They are verbatim, so an editor's note now explains that the audit was dropped. results.md was updated the same way.
2. **Pre-registration:** the claim is dropped. "Pre-registered" wording was replaced with "frozen and hashed before data collection (not publicly time-stamped in advance)" in the paper and results.md. `prereg_manifest.md` became `config_hashes.md`.
   - `protocol.md` and `brief.md` are left byte-identical, so their hashes still verify. They therefore keep the old wording, which is noted in `config_hashes.md` and the README.
   - The verbatim debate files carry an editor's note.
3. **Hash check:** `run_experiment.py` changed after the freeze (debate resume cache and consensus token limit). I reconstructed the frozen version by reversing those two edits. It matches the frozen hash exactly (`5119e4b3…`) and is published as `run_experiment_frozen.py`, with the diff in `config_hashes.md`.
4. **Rachel Held Evans:** I checked that the paper implies no personal connection. It only quotes her book, as the epigraph and in one analytical sentence.
5. **Byline:** Mike's ORCID was added.
6. **Links:** appendix links now point to https://github.com/michaelbaird/tribe-in-the-machine.
7. **Charts:** the paper now embeds the SVG charts (identical content to the PNGs), so they render on GitHub.
