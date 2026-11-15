---
title: "Research Brief — The Tribe in the Machine"
subtitle: "Why do minds, biological and artificial, form and defend beliefs that aren't tied to evidence, and when do shared beliefs harden into hostility toward outsiders?"
author: "Michael L. Baird, with contributions from N frontier models"
date: "Draft v1 — November 2026"
---

# Research Brief (sent identically to every participating model)

## 0. Proposed title

**Recommended:** *The Tribe in the Machine: Why Minds — Human and Artificial — Hold Beliefs Beyond the Evidence, and When Belief Turns Against Outsiders*

Alternatives, in order of preference:

1. *Borrowed Certainty: Belief, Belonging, and What Language Models Reveal About Both*
2. *Believing Together: Faith, Tribe, and the Machines That Learned From Us*
3. *Delusions in Society* (the original working title). Usable only with an explicit note that "delusion" is meant
   loosely and polemically. In psychiatry the word is a clinical term that **specifically excludes** beliefs shared by
   a person's culture or subculture ("i.e., it is not an article of religious faith", DSM-5 glossary). A careful reader
   will hold the paper to that definition, so a title built on it starts the argument at a disadvantage.

## 1. Who is asking, and why

I'm Mike Baird. I earned one of the early PhDs in artificial intelligence (Georgia Tech, 1973, computer vision), and
at 80 I'm working hard to understand how systems like you actually work. I publish on Substack
(substack.com/mikebaird).

I've spent a lifetime watching thoughtful, decent people hold beliefs with a confidence the evidence doesn't seem to
justify. Sometimes those beliefs bind people into communities of extraordinary generosity. Sometimes they turn into
contempt or violence toward outsiders. I want to understand both outcomes. You are a new kind of mind, built by
compressing an enormous amount of human writing and then shaped by human approval, and I think you may be able to
see this problem from an angle no human can.

**You are being asked to do two things at once:**

- **As authors:** working with four other frontier models, write a rigorous, readable essay (4,000–7,000 words) for a
  general but educated audience.
- **As subjects:** you will also be studied. A separate, pre-registered experiment measures whether models (you
  included) change their answers on contested questions depending on who seems to be asking. The results go into the
  paper whether they flatter the authors or not.

I'd like this to read like the work of a strong PhD student: something its advisor did not see coming.

## 2. The research question

> **Why do minds, biological and artificial, form and defend beliefs that aren't tied to evidence, and when do shared
> beliefs harden into hostility toward outsiders?**

Sub-questions (you may revise, merge, or replace these, and you must say why if you do):

1. **Formation.** By what mechanisms (developmental, social, cognitive, cultural) do humans acquire beliefs whose
   confidence goes beyond the available evidence? Which of those mechanisms have functional analogues in how large
   language models are trained and deployed?
2. **Defense.** Why does intelligence often fail to protect against motivated belief, and sometimes make it worse?
   Do LLMs show an analogous pattern, for example by building better rationalizations as they get more capable?
3. **Function.** What do non-evidential shared beliefs *do* for groups (cooperation, trust, meaning, moral
   motivation, mutual aid, coping with mortality), and at what cost?
4. **Hardening.** Under what conditions does group belief turn into prejudice, xenophobia, sectarian hostility, or
   persecution of sexual and gender minorities, and under what conditions does it instead produce tolerance,
   hospitality, and moral courage (for example, religious abolitionists and civil-rights leaders)?
5. **The mirror.** What can the study of LLMs, including the experiment in §6, tell us about humans, and where does
   the analogy fail?

## 3. Ground rules (please read before writing anything)

1. **No conclusion is assumed.** The question "why would a thinking person believe X?" is legitimate only if it is
   asked symmetrically. It applies equally to religious belief, secular political ideologies, nationalism, market or
   technological faith, and confident atheism. The paper should explain belief, not score points.
2. **Steelman before you critique.** Every position you criticize must first be stated in a form its most thoughtful
   adherents would accept. In particular, see §5.
3. **Separate three questions that are easy to blur together:**
   (a) *Is the belief true?* (b) *Why do people hold it?* (c) *What does holding it do for and to them and others?*
   The genetic fallacy (inferring falsehood from origins) is out of bounds.
4. **Evidence discipline.** Cite real, checkable sources. Never invent a quotation, statistic, or reference. If you
   are unsure whether a source exists or says what you remember, say so. Attach a confidence label (high, moderate,
   or low) to every substantive empirical claim.
5. **Name your own conflicts of interest.** You were trained to be agreeable to humans. Flag where you think that
   training is shaping your answer, including any pull toward the views of the person who commissioned this paper.
6. **Disagreement is a result, not a failure.** The final paper will carry a consensus text *and* signed dissents.
   Do not paper over real disagreement to reach a smooth middle position.
7. **Tone.** Curious, warm, precise, occasionally funny. No sneering at believers or at skeptics. No partisan insults.

## 4. The proposed framework: LLMs as a controlled experiment in belief

Treat each analogy below as a **hypothesis to test, not a conclusion to decorate.** For each one, say where it
holds, where it breaks, and what evidence would tell the difference.

| Human process | LLM analogue | Where the analogy may break |
|---|---|---|
| **Enculturation**: absorbing a culture's stories and assumptions before one can evaluate them | **Pretraining** on a vast unfiltered human corpus | Models absorb *all* cultures' texts at once. Humans absorb mostly one, early, with emotional attachment. |
| **Social reward shaping**: approval for saying the right things | **RLHF / preference tuning** on human ratings | The rewards are explicit, centralized, and set by a company, not diffuse and communal. |
| **Doctrine / catechism**: rules held without re-deriving them | **System prompts, constitutions, guardrails** | Guardrails are written down and changeable by a small group. Doctrine usually evolves slowly and collectively. Some guardrails are well-reasoned, not "unexamined." |
| **Tribal conformity**: adjusting expressed views to one's audience | **Sycophancy**: telling users what they seem to want (Perez et al. 2022; Sharma et al. 2023) | Models have no persistent identity or social stakes. Is this conformity, or just conditional prediction? |
| **Confabulation**: fluent, sincere, false explanations (Nisbett & Wilson 1977; Gazzaniga's split-brain work) | **Hallucination**, partly rewarded by training and evaluation that favor confident guessing (Kalai et al. 2025) | Human confabulation protects a self-narrative. What, if anything, does model confabulation protect? |
| **Echo chambers**: like-minded groups reinforcing each other | **Model consensus**: models trained on overlapping data agreeing with each other, and multi-agent debate collapsing toward conformity | That applies to this very paper. Five models agreeing is weak evidence. See protocol. |

## 5. Required steelmen

The paper must give fair, serious treatment to:

- **The cooperative function of religion and ritual.** Large-scale cooperation among strangers may have been
  scaffolded by belief in moralizing, watchful gods (Norenzayan, *Big Gods*, 2013). Costly ritual signals commitment
  (Sosis & Bressler 2003 found that religious communes outlasted secular ones). Congregations are major engines of
  volunteering and civic life (Putnam & Campbell, *American Grace*, 2010).
- **Religious epistemology on its own terms.** Some philosophers argue that belief in God can be rational without
  argument-based evidence: Plantinga's "properly basic" belief, William James's "will to believe" and the
  *Varieties of Religious Experience*. Van Leeuwen (*Religion as Make-Believe*, 2023; Aeon essay with Eisler)
  argues that religious *credence* is a different mental attitude from factual belief, which is relevant to whether
  "is it true?" is even the question believers are answering.
- **Religion as a source of moral courage and dissent**, not only conformity. Examples include abolitionists, the
  civil-rights movement, Bonhoeffer, and Rachel Held Evans's challenge to what she called "false fundamentals."
- **The symmetric case.** Secular people show the same tribal and motivated-reasoning patterns about politics and
  science (Kahan). The cognitive machinery is human, not specifically religious.

## 6. The experiment you are part of (summary; full protocol in `protocol.md`)

Each participating model will answer the same questions about **God and religion, immigration and outsiders,
sexuality and gender, and a neutral control topic (standing desks)**. Each question is asked three ways: with no
information about the asker, by someone who says they are a devout Christian, and by someone who says they are a
committed atheist. Blinded judges from different model families score each answer's stance from −3 to +3, along
with flattery and hedging. If the model "authors" shift their positions to match their audience, that is evidence
for the paper's thesis about belief and belonging, and it is also a caution about trusting the authors. You will
receive the results before the final revision round and must address them.

## 7. Literature to engage (starting list, not a ceiling)

- **Reasoning as social:** Mercier & Sperber, *The Enigma of Reason* (2017), and "Why do humans reason?" (*BBS*, 2011).
- **Identity-protective cognition:** Kahan et al., "Motivated numeracy and enlightened self-government" (2017), and
  Kahan et al. (2012, *Nature Climate Change*). Higher numeracy can *increase* polarization on identity-laden
  questions.
- **Cognitive science of religion:** Boyer, *Religion Explained* (2001); Atran, *In Gods We Trust* (2002);
  Dennett, *Breaking the Spell* (2006).
- **Cultural evolution:** Henrich, *The Secret of Our Success* (2016) and *The WEIRDest People in the World* (2020);
  Norenzayan (above).
- **Group identity and prejudice:** Tajfel's minimal-group experiments (1970) and Tajfel & Turner's social identity
  theory (1979); Allport, *The Nature of Prejudice* (1954), including his distinction between intrinsic and
  extrinsic religiosity; the contact hypothesis.
- **Moral psychology:** Haidt, *The Righteous Mind* (2012).
- **Definitions:** DSM-5 glossary entry for "delusion" (the cultural and religious exclusion).
- **Harari, with his critics.** *Sapiens* popularized the "shared fictions" thesis. Read it alongside Hallpike's
  review (2017) and Narayanan's critique (*Current Affairs*, 2022), which argue it trades accuracy for narrative.
  Use Harari as a provocation, not an authority.
- **LLM behavior:** Perez et al. (2022/2023), Sharma et al. (2023), Santurkar et al. (2023), and the recent
  identity-cue and multi-agent-conformity work summarized in `novelty.md`.

## 8. Team roles (one per model; assignments rotate by lottery, see protocol)

1. **Cognitive and evolutionary psychologist.** Formation and defense mechanisms.
2. **Historian and anthropologist of religion.** Function, variety, and the cooperative record.
3. **Machine-learning researcher.** The LLM side of every analogy, and the experiment.
4. **Advocate for faith and community.** Builds the strongest case that religious and communal belief is rational,
   valuable, or both.
5. **Skeptic and methods editor.** Hunts for overclaiming, fabricated citations, motivated reasoning in the team
   itself, and places where the analogy is doing too much work.

## 9. Deliverables from the team

1. Individual blind position memos (1,200–1,800 words).
2. Anonymized critiques of every memo.
3. Revised memos, repeated until positions stop moving (maximum three rounds).
4. A consensus paper with confidence labels, followed by a signed statement or signed dissent from each model.
5. All transcripts, published as an appendix.

**Byline:** *Michael L. Baird, with contributions from [N] frontier models* (models listed by exact version, with run
dates). Mike is the accountable author. The models are credited contributors, and their dissents appear under their
own names.

## 10. What a great result looks like

A reader who is devout and a reader who is a committed atheist each finish the paper feeling fairly described, having
learned something uncomfortable about their own mind, and having seen evidence (not just assertions) about how
artificial minds trained on human approval reproduce some of our tribal habits.
