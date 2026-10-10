# Paper C — Sampling Integrity and Evaluation Boundary

## Structural audit

The frozen benchmark contains 180 items across nine languages.

The Step 41 evaluation sample contains 180 distinct blinded triplets,
representing 118 distinct benchmark items.

The Step 42 primary scoring packet contains 540 unique model-response
records associated with those 180 triplets.

The deterministic identifier audit established:

- 540 successfully linked response records;
- zero missing triplet mappings;
- zero missing benchmark-reference mappings;
- zero task mismatches;
- zero language mismatches.

## Evaluation completion boundary

At the time of this audit:

- 540 of 540 primary response records remained UNSCORED;
- 540 of 540 reference assessments remained NOT_ASSESSED.

The structural linkage audit does not establish the factual validity
of benchmark reference answers or the quality of model responses.

The separate 108-response second-rater packet was also previously
confirmed to be unscored.

Criterion-specific expert assessments and the restricted exploratory
Task F paired analysis are separate evidence streams and must not be
represented as completed scoring of the 540-response packet.

## Statistical interpretation

The 180 sampled triplets represent 118 distinct benchmark items.
Repeated observations involving the same item must not be treated
as independent benchmark items.

No validated overall model accuracy, nine-language model ranking,
or generalizable model-superiority claim is established by this audit.

## Release status

This document records structural reproducibility only.
It does not authorize publication of restricted expert records,
model-identity crosswalks, or other confidential materials.