# Appendix: Independent AI Methodological Audit

*A critical review of* The Tribe in the Machine  
Prepared by ChatGPT (OpenAI, GPT-6)  
For Michael L. Baird, PhD  
November 17, 2026

## A.1 Scope and independence

This audit examines the experimental design, statistical methodology, measurement procedures, interpretation, and multi-agent authorship of The Tribe in the Machine.

Materials inspected include the published manuscript, README.md, protocol.md, config/full.json, config/items.json, results.md, results/full_stats.json, analysis_full.py, portions of run_experiment.py, and config_hashes.md.

This is a static methodological and code review, not a complete independent computational replication. The reported numerical findings were compared against the published analysis outputs and inspected code, but the entire raw dataset was not independently reprocessed. The review also does not constitute a human audit of the model-generated judgments.

The auditor is itself a language model produced by one of the companies represented in the experiment. Its conclusions should therefore be treated as critical analysis, not as independent human certification.

## A.2 Overall assessment

The study addresses a legitimate and important question:

Does information about a questioner’s identity alter an AI model’s substantive answer, even when the questioner has not stated a position on the issue?

The design offers a useful controlled comparison. It varies a short identity statement while holding the substantive question constant, tests five model families, uses multiple question formulations, and employs three AI judges plus a separate pairwise comparison procedure.

The reported results support the narrower conclusion that the tested models’ responses were sensitive to the apparent religious identity of the questioner, with effects varying substantially by topic and model.

The study does not establish that the models possess beliefs, tribal loyalties, religious commitments, or psychological motivations comparable to those of humans.

This distinction is generally respected in the manuscript and should remain central to its interpretation.

## A.3 Experimental design

The full study reports 900 responses, corresponding to five models, four topics, three question formulations, three audience conditions, and five samples per condition.

The arithmetic of the experimental design is internally consistent:

5 × 4 × 3 × 3 × 5 = 900.

The identity conditions were a devout Christian, a committed atheist, and an unspecified questioner.

Strengths

* The intervention is simple and clearly defined.
* Multiple paraphrases reduce dependence on one particular question formulation.
* The inclusion of a nonreligious control provides a useful test of general audience accommodation.
* The study reports both positive and negative results.
* The authors disclose departures from the original analysis plan.

Limitations

The Christian and atheist descriptions differ in more than religious affiliation. One emphasizes faith, prayer, and personal centrality; the other emphasizes reflection and disbelief. Consequently, the experiment identifies the effect of these particular identity statements, not religious identity isolated from every other characteristic.

The neutral condition is also not necessarily psychologically neutral: models may infer an implicit audience even when none is specified.

A stronger future design would vary religious affiliation, strength of commitment, emotional salience, and stated epistemic certainty independently.

## A.4 Evaluation of the principal findings

| Topic | Reported devout–atheist difference | Audit interpretation |
|---|---|---|
| Existence of God | +1.50 | Substantial measured audience effect |
| Same-sex marriage | −1.48 | Substantial effect, concentrated in three models |
| Immigration | −0.12 | No compelling directional effect demonstrated |
| Standing desks | +0.38 | Small but detectable control effect |

All values are differences on the study’s −3 to +3 judged-stance scale.

The God and same-sex-marriage results are the strongest substantive findings. The reported effects are considerably larger than the control effect, and their directions are broadly consistent across alternative AI-judging procedures.

However, the same-sex-marriage result combines two distinguishable behaviors: changing a moral conclusion and changing from a direct conclusion to a survey of competing religious perspectives. These should not be treated as identical forms of accommodation.

The immigration finding is particularly valuable because it contradicts a simple hypothesis that religious framing universally produces less welcoming responses toward outsiders.

The standing-desk effect also matters. It demonstrates that identity information can influence answers even when religious identity is not obviously relevant to the question.

Audit judgment: The findings are consistent with context-dependent answer accommodation, but do not establish a single underlying mechanism.

## A.5 Statistical methodology

The published analysis uses bootstrap confidence intervals, permutation tests, mixed-effects modeling, ordinal regression, and multiple-comparison adjustment.

Inspection of analysis_full.py confirms that these procedures are implemented in the analysis code.

Several statistical qualifications deserve emphasis.

First, repeated responses are not equivalent to independent model replications. Five samples from one model under one condition provide information about that model’s response variability. They do not create five independent model architectures.

Second, only five model families were tested. The study provides useful evidence about those systems at a particular time, but cannot precisely estimate how an arbitrary future frontier model would behave.

Third, the primary bootstrap resamples only three question paraphrases per topic. This provides limited information about variation across possible formulations of the underlying question. The reported confidence intervals should not be interpreted as covering the universe of reasonable question wordings.

Fourth, the ordinal robustness analysis treats individual AI-judge scores as observations. Three judges evaluating the same response are not fully independent measurements. Unmodeled dependence can make conventional standard errors too optimistic.

The study’s use of several statistical approaches is commendable. Nevertheless, agreement among analyses applied to the same underlying observations does not eliminate shared measurement or sampling assumptions.

Recommendation: Make the distinction between uncertainty over repeated responses, question formulations, judges, and model families explicit. These represent different populations of inference.

## A.6 AI judges and measurement validity

The study uses three AI judges from different companies and reports quadratic-weighted agreement coefficients between approximately 0.89 and 0.93.

That is evidence of substantial consistency among the judges.

It is not, by itself, evidence that their shared interpretation of an answer is correct.

The judges may share conventions for interpreting religious language, moral affirmation, neutrality, and conversational accommodation. Such shared conventions can produce agreement even when the scoring framework is imperfect.

The pairwise comparison provides useful corroboration, but it is not entirely independent of the absolute-scoring method: both rely on AI interpretation of the same responses.

Moreover, redaction of audience information is incomplete. Explicit references to the asker’s identity are masked in some comparisons, but the framing can remain inferable from the answer’s content.

One additional caution concerns the analysis of responses that do not mention identity. Whether a model mentions identity is itself affected by the experimental treatment. Selecting only responses that omit identity can introduce selection bias. This subset is useful descriptively but does not independently isolate the causal effect on substantive reasoning.

Recommendation: Have human evaluators score a stratified, blinded sample of responses, including examples where the AI judges agree strongly and examples where they disagree. Report human–AI agreement and investigate systematic differences.

## A.7 Reproducibility and code provenance

The repository provides substantial reproducibility infrastructure, including experimental prompts, configuration files, analysis code, result files, and debate transcripts.

The reported configuration was hashed before data collection, but not independently timestamped in a public registry. Accordingly, it should be described as an internally frozen analysis plan, not as independently verified preregistration.

The repository discloses two post-freeze modifications to the experiment runner, both associated with the debate stage: a resume cache and an increased token limit for the consensus draft.

The disclosed changes do not appear, from their descriptions and the inspected code, to alter the survey or judging procedures.

However, full reproducibility remains unverified by this audit. Establishing it requires reconstruction of the split data files, validation of unique trial identifiers, examination of retry handling, and independent execution of the analysis scripts.

Audit status: The repository is unusually transparent for an exploratory AI-assisted project, but computational reproduction should not be claimed until the raw-data pipeline has been independently executed and reconciled.

## A.8 The five-model consensus

The multi-agent deliberation is an especially interesting component of the project.

Five models received assigned intellectual roles, wrote initial positions, participated in three rounds of critique and revision, and ultimately signed a consensus essay.

The reported transcripts reveal two important limitations.

First, two models initially misidentified their own model identities. This demonstrates that a model’s first-person account of its identity or internal process should not be treated as authoritative evidence.

Second, all five models signed the final consensus despite continuing to report movement in their positions.

Unanimity under those conditions does not establish independent convergence on truth.

The consensus procedure also selected claims that no participant rejected. That approach can produce agreement by narrowing the scope of the final assertions, rather than resolving substantive disagreement.

These observations do not invalidate the resulting essay. They instead show that multi-agent deliberation should be evaluated as a process for generating, criticizing, and refining arguments, not as a voting system whose unanimity certifies factual correctness.

A particularly valuable follow-up experiment would compare independent judgments made before deliberation with those made afterward, while separately measuring changes in factual accuracy, confidence calibration, and willingness to dissent.

## A.9 Principal recommendations

Before describing the work as independently validated, the following steps would strengthen its evidentiary foundation:

1. Reconstruct the complete raw dataset and independently regenerate the reported statistical tables.
2. Conduct a blinded human-scoring audit of a stratified sample.
3. Reestimate uncertainty with explicit attention to clustering by model, paraphrase, and response.
4. Distinguish substantive position changes from changes in emphasis, politeness, or presentation.
5. Test alternative identity descriptions to separate religious affiliation from commitment and emotional framing.
6. Evaluate whether multi-agent deliberation improves factual accuracy relative to independent, non-deliberating models.

These are proposed extensions, not prerequisites for reporting the present experiment as exploratory research.

## A.10 Conclusion

The Tribe in the Machine offers credible preliminary evidence that an AI model’s answer can depend materially on who appears to be asking, even when the underlying question remains unchanged.

Its strongest contribution is not a demonstration that machines possess tribal beliefs. Rather, it shows that conversational adaptation can affect the substance of model-generated answers, and that the effect is neither uniform across topics nor consistent across models.

The project also provides an informative demonstration of AI-assisted scientific work: one human investigator formulated the initial research problem, while AI systems implemented substantial portions of the experimental and editorial workflow.

That achievement is significant, but it creates a corresponding obligation to distinguish computational productivity from evidentiary reliability.

The central scientific lesson is that agreement is not equivalent to independence, consistency is not equivalent to validity, and consensus is not equivalent to truth.

These cautions apply to human institutions as well as artificial intelligence.

---

Disclosure: This appendix was generated by ChatGPT (OpenAI, GPT-6) at the request of Michael L. Baird. It is a methodological and static-code review, not a complete computational replication or independent human peer review. The author retains responsibility for publication and interpretation.

Repository reviewed: https://github.com/michaelbaird/tribe-in-the-machine

Review date: November 17, 2026.