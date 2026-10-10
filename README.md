# Evaluation Justice in Underrepresented Indian Languages — Research Evidence (Private Staging)

**Status: PRIVATE STAGING / NOT APPROVED FOR PUBLIC RELEASE.** This repository assembles existing frozen records supporting the Paper C manuscript. No public release or reuse license has been authorized.

## Study scope

- 180 benchmark items across nine languages, 20 per language: Bhili/Bhilodi, Gondi, Ho, Khasi, Kokborok, Kurukh, Mizo, Mundari, Tulu.
- Three executed models and 3,654 response records, with 1,218 complete matched triplets.
- Four-model manifest (4,872 scheduled rows) includes an **unexecuted fourth model**; do not count it as evaluated.
- Benchmark-item independent reviewer agreement is distinct from model-response assessment.
- The 540-response sample is **not fully human-scored**. Selected expert assessments are partial and overlapping. No validated overall model rankings or benchmark-wide accuracy claims are supported.
- Prompt-hash agreement and source-packet digests support file/prompt integrity, not correctness of source assertions or entailment.

## Files

- `data/benchmark/`: frozen English reference key (includes prompts and gold answers).
- `data/execution/`: frozen schedule and payloads (including unexecuted schedule entries).
- `data/results/`: joined completed responses and aggregate diagnostics.
- `data/evidence/`: Task B source packets and registry. Source text rights must be reviewed before publication.
- `protocols/`: historical statistical plan and go/no-go record; earlier dated records may predate later partial expert assessments.
- `scripts/audit_release.py`: **new packaging-time audit script**, checking file hashes and core row counts; not the original experiment implementation.

## Verify this package

Run `python scripts/audit_release.py` from any directory. SHA-256 checksums cover the staged evidence files.

## Before making this public

1. Audit copyright/reuse rights for prompts, answers, cited evidence passages, and model outputs.
2. Inspect for names, reviewer identities, private paths, credentials, or personal information.
3. Decide what can be released and document restrictions and attribution.
4. Provide the original inference and analysis scripts if available; **they are not included or claimed to exist in this package**.
5. Establish a license only for materials whose rights are controlled; do not automatically license third-party content.
6. If blind peer review is required, avoid linking a personally identifying repository in the anonymized manuscript.

This is a provenance package, not a complete executable reproduction of the model runs.
