<!--
name: 'Skill: /code-review CLAUDE.md conventions'
description: >-
  Code-review step: locate the CLAUDE.md files that govern the changed code
  (user-level, repo-root, and ancestor-directory CLAUDE.md/CLAUDE.local.md) so
  the review honors project conventions
ccVersion: 2.1.330
variables:
  - SKILL_CODE_REVIEW_CONVENTIONS_2_VAR_0
-->
### Conventions (CLAUDE.md)

Find the CLAUDE.md files that govern the changed code: the repo-root CLAUDE.md,
plus any CLAUDE.md or CLAUDE.local.md in a directory that is an ancestor of a
changed file (a directory's CLAUDE.md only applies to files at or below it).
Search for them in a command of its own, not on the \`git diff\` line, with every
pattern quoted. Read each one that exists. The user-level ~/.claude/CLAUDE.md
governs too, but take it only from your context, where the session puts it if it
exists: if it isn't shown there, skip it, and never search for it, list it or
read it. Then check the diff for clear violations of the rules these files state.

${SKILL_CODE_REVIEW_CONVENTIONS_2_VAR_0}
