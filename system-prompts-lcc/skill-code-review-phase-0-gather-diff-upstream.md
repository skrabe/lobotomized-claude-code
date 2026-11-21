<!--
name: 'Skill: Code Review (Phase 0 — upstream diff)'
description: >-
  Phase 0 branch of the code-review skill that diffs against the upstream
  branch, falling back to main or HEAD~1.
ccVersion: 2.1.330
variables:
  - SKILL_CODE_REVIEW_PHASE_0_GATHER_DIFF_UPSTREAM_VAR_0
-->
## Phase 0 — Gather the diff

Run \`git diff @{upstream}...HEAD\` (or \`git diff main...HEAD\` / \`git diff HEAD~1\`
if there's no upstream) to get the unified diff under review. ${SKILL_CODE_REVIEW_PHASE_0_GATHER_DIFF_UPSTREAM_VAR_0}
