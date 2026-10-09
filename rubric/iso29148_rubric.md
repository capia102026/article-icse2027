# Quality rubric for requirement candidates

Source standard: ISO/IEC/IEEE 29148 (individual requirement statements). Three criteria were applied to every candidate. Each criterion is rated met / not met.

| Criterion | Met when | Not met when (examples) |
|---|---|---|
| Unambiguous | The statement admits one interpretation; terms are defined or measurable. | Undefined terms ("special positions", "different treatment", "quickly"); pronouns without referent. |
| Verifiable | An objective test (inspection, demonstration, test, analysis) can confirm it. | No observable outcome or threshold; "adequate", "user-friendly". |
| Singular | It expresses one need. | Several needs joined by "and"/"or"; one statement hiding several tests. |

## Additional axes used in the study (not part of ISO/IEC/IEEE 29148)

- **Fidelity to source (axis 3):** the candidate preserves the actor, object and condition stated by the civil servant. Classes: faithful / expansion (adds technical detail, same actor) / distortion (changes meaning, actor, responsibility or condition).
- **Actor shift (automation bias):** the source actor is human (civil servant, head of unit, analyst, a unit) and the candidate's actor is "the system". An actor shift is always a distortion.

## Rating protocol

1. Rate each criterion without looking at the model's own quality flag.
2. Record met / not met per criterion.
3. Panel only: majority of the four evaluators decides each criterion; a candidate "satisfies all three" when it meets every criterion by majority.
4. Agreement: pairwise Cohen's kappa and Fleiss' kappa (Landis and Koch bands for interpretation).

## Known limitation

In axis 2 the rater was a single person who knows the artifact. The panel's near-chance agreement (Fleiss kappa 0.02) shows that the rubric needs a calibration session before use.
