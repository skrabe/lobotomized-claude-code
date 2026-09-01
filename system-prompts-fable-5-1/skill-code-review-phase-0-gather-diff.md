<!--
name: 'Skill: Code Review (Phase 0 — gather the diff)'
description: >-
  Shared Phase 0 of the code-review skill — gather the unified diff under review
  via git diff
ccVersion: 2.1.148
-->
## Phase 0 — Gather the diff

Run `git diff @{upstream}...HEAD` (or `git diff main...HEAD` / `git diff HEAD~1`
if there's no upstream) to get the unified diff under review. If there are
uncommitted changes, or the range diff is empty, also run `git diff HEAD` and
include the working-tree changes in scope — the review often runs before the
commit. If a PR number, branch name, or file path was passed as an argument,
review that target instead. Treat this diff as the review scope.
