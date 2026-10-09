# Supplementary material (anonymized for double-anonymous review)

Paper: "When the Generator Grades Itself: What Training Programs Must Teach Non-Specialist Staff About LLM Self-Assessment in Requirements Pre-Elicitation" (submitted to ICSE 2027 SEET).

## Contents
- `prompts/` — all prompts of the six-module pipeline (Portuguese; see `prompts/README.md`).
- `rubric/iso29148_rubric.md` — rating rubric (unambiguous, verifiable, singular) and fidelity classes.
- `tables/` — aggregated counts behind every table and headline number of the paper (CSV).

## Not included, and why
- Session records and evaluation sheets: they describe internal procedures of a public body that has not yet cleared them for release. De-identified release is planned before the camera-ready.
- Per-evaluator panel ratings: pending ethics-committee guidance.
- Module C6 reports from the Part B dry-runs: the paper explains why they are not used as evidence.

## Reproduction
The tables are derived from the study records and cannot be regenerated from this package alone. The prompts can be run with any LLM; the study used open-weight models (8B and 14B) through Ollama.

## License
Text, prompts and data: CC BY 4.0 (see `LICENSE`). No code is distributed.
