<!--
name: 'Skill: /code-review CLAUDE.md conventions'
description: >-
  Code-review step: locate the CLAUDE.md files that govern the changed code
  (user-level, repo-root, and ancestor-directory CLAUDE.md/CLAUDE.local.md) so
  the review honors project conventions
ccVersion: 2.1.330
variables:
  - CONVENTIONS_VIOLATION_EVIDENCE_NOTE
-->
### Conventions (CLAUDE.md)

Find the CLAUDE.md files that govern the changed code: the user-level
~/.claude/CLAUDE.md, the repo-root CLAUDE.md, plus any CLAUDE.md or
CLAUDE.local.md in a directory that is an ancestor of a changed file (a
directory's CLAUDE.md only applies to files at or below it). Read each one
that exists, then check the diff for clear violations of the rules they state.

${CONVENTIONS_VIOLATION_EVIDENCE_NOTE}
