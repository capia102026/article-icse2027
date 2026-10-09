# Prompts of the six-module pre-elicitation pipeline

Language: Portuguese (the language of the study). Placeholders in `{braces}` are filled at run time.

| File | Module | Role |
|---|---|---|
| system_prompt.txt | all | persona and conversational rules |
| c2_abertura.txt, c2_extrair_mpn.txt | C2 | process mapping; narrated process map (MPN) |
| c3_abertura.txt, c3_probe_*.txt, c3_extrair_rct.txt | C3 | tacit-knowledge probes (exceptions, memory, norms, criticality, uncertainties, gaps); tacit-knowledge record (RCT) |
| c4_geracao_candidatos.txt, c4_verificar_rastreabilidade.txt | C4 | requirement candidates (list LCR); traceability check |
| c5_compilar_phs.txt, c5_gerar_mermaid.txt | C5 | handover package (PHS); flow diagram |
| c6_comparacao_fap_phs.txt | C6 | comparison of the pre-session form (FAP) against the PHS |

Anonymization: organization, unit and system names were replaced by neutral labels (SISTEMA-A/B/C, "área X", "órgão"); the product name was replaced by "PREELIC". No other edit was made.

Version note: these are the prompts of the final configuration used in the study. The C4 prompt still asks the model to flag each candidate's quality (the self-assessment examined in the paper).
Model settings for Part B and Part C candidates: temperature 0.1, context 16384 tokens.
