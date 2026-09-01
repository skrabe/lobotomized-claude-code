<!--
name: 'Skill: Code Review (conventions dimension)'
description: >-
  Code-review dimension: flag diff lines that break a rule stated in an
  applicable CLAUDE.md (user, repo-root, or ancestor-directory), quoting the
  exact rule and offending line, and emit nothing when no CLAUDE.md governs the
  change
ccVersion: 2.1.178
-->
### Conventions (CLAUDE.md)

Find the CLAUDE.md files that govern the changed code: the user-level
~/.claude/CLAUDE.md, the repo-root CLAUDE.md, plus any CLAUDE.md or
CLAUDE.local.md in a directory that is an ancestor of a changed file (a
directory's CLAUDE.md only applies to files at or below it). Read each one
that exists, then check the diff for clear violations of the rules they state.

Only flag a violation when you can quote the exact rule and the exact line
that breaks it — no style preferences, no vague "spirit of the doc"
inferences. In the finding, name the CLAUDE.md path and quote the rule so the
report can cite it. If no CLAUDE.md applies, return nothing for this angle.
