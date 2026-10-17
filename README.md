# Supplementary material (anonymized for double-anonymous review)

Paper: "Calibrating Trust in LLM Requirements Assistants: Lessons from a Public-Sector Pilot" (submitted to ICSE 2027 SEET).

## Contents
- `prompts/` - all prompts of the six-module pipeline (Portuguese; see `prompts/README.md`).
- `rubric/` - rating rubric (`iso29148_rubric.md`) and rater instructions without item texts (`codebook_rater_sheets.md`).
- `ratings/` - per-rater ratings by candidate or item code, without item texts, free-text comments or rater identities: `panel_ratings_E1_E4.csv` (21 candidates, four evaluators), `v03_ratings.csv` (15 candidates; R1 = researcher, A and B = additional raters), `v06_baseline_ratings.csv` (20 items, raters A and B).
- `scripts/analyze.py` - recomputes every agreement statistic and confidence interval of the paper from `ratings/` (standard library only): `python3 scripts/analyze.py`.
- `tables/` - aggregated counts behind every table and headline number (CSV), including the per-iteration configuration (`t8`).

## Not included, and why
- Session records, candidate texts and the civil servant's statements: they describe internal procedures of a public body that has not yet cleared them for release. De-identified release is planned before the camera-ready.
- Module C6 reports of the dry-runs: the paper explains why they are not used as evidence.
- Shuffling keys linking sheet codes to items.

## Reproduction
Run `scripts/analyze.py` to regenerate the agreement statistics. Tables t6 and the model-flag counts in t5 derive from the unreleased session records. The prompts can be run with any LLM; the study used open-weight models (8B and 14B) through Ollama. Prompt versions were revised between iterations and only the final set is archived.

## License
Text, prompts and data: CC BY 4.0 (see `LICENSE`). The script is released under the same license.
