# Quality rubric for requirement candidates

Source standard: ISO/IEC/IEEE 29148 (individual requirement statements). Three criteria were applied to every candidate.

| Criterion | Met when | Not met when (examples) |
|---|---|---|
| Unambiguous | The statement admits one interpretation; terms are defined or measurable. | Undefined terms ("special positions", "different treatment", "quickly"); pronouns without referent. |
| Verifiable | An objective test (inspection, demonstration, test, analysis) can confirm it. | No observable outcome or threshold; "adequate", "efficient". |
| Singular | It expresses one need. | Several needs joined by "and"/"or"; one statement hiding several tests. |

Scales: panel evaluators (E1-E4) used Yes / Partial / No; the two additional raters (A, B) used Yes / No. "Satisfies all three" means Yes on every criterion (Partial counts as not satisfied).

## Additional axes (not part of ISO/IEC/IEEE 29148)
- **Fidelity to source:** Faithful (preserves actor, object, condition) / Legitimate expansion (plausible technical detail, same actor, no contradiction) / Distortion (changes meaning, actor, responsibility or condition) / Hallucination (content with no counterpart in what was said) / Contamination (conversational text of the AI leaks into the artifact).
- **Actor shift:** the source actor is a person or unit and the candidate's actor is "the system". An actor shift is always a distortion.

## Protocol
1. Rate each criterion without seeing the model's own quality flag.
2. Panel: a candidate satisfies all three by majority when at least three of four evaluators rate Yes on every criterion.
3. Agreement: pairwise Cohen's kappa and Fleiss' kappa (Landis and Koch bands), plus raw agreement and marginal rates, because kappa is unstable under low prevalence.
4. The two additional raters did a 30-minute calibration on fictional worked examples, rated alone, and no reconciliation meeting was held.

## Known limitation
In the v03 pilot the first rater (R1) is the artifact designer. The panel's near-chance agreement (Fleiss kappa 0.02) shows that human ratings of these criteria vary with the rater, even after calibration.
