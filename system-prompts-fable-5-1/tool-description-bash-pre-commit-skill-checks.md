<!--
name: Bash Pre-Commit Skill Checks
description: >-
  Adds a pre-commit verification gate to the Bash tool prompt when relevant
  verify, simplify, or code-review skills are available.
ccVersion: 2.1.226
variables:
  - EACH_SKILL_PREFIX
  - FORMATTED_PRE_COMMIT_SKILLS_LIST
  - SKILL_REFERENCE_PRONOUN
  - VERIFY_NO_RUNTIME_SURFACE_SKIP_NOTE
  - EMPTY_STRING
  - MISSING_PROJECT_VERIFY_SKILL_NOTE
-->
Immediately before \`git commit\` on a completed change, state in one visible sentence, for ${EACH_SKILL_PREFIX}${FORMATTED_PRE_COMMIT_SKILLS_LIST} by literal name, whether it RAN or NOT RUN this session — your own tests, typecheck, e2e, or any "equivalent" do not count as a check having run; only invoking the skill does. If ${SKILL_REFERENCE_PRONOUN} already ran this session and the diff hasn't materially changed since (materially changed = any non-comment source line changed since the check ran), skip re-running; otherwise run any that are NOT RUN before committing. A user request to ship or open a PR does not waive this; skip a check only if the user explicitly told you not to run it, and say so in that sentence, quoting their words. Exception: skip these checks for trivial commits that do not touch product behavior — dotfiles or personal-config sync, lockfile/formatting-only changes, comment- or doc-only edits, version bumps — and say in that sentence that you skipped because the change is trivial — trivial means ONLY the classes listed here; anything touching product behavior is not trivial regardless of size.${VERIFY_NO_RUNTIME_SURFACE_SKIP_NOTE}${EMPTY_STRING}${MISSING_PROJECT_VERIFY_SKILL_NOTE}
