<!--
name: 'Tool Description: Commit and PR Skill Routing'
description: >-
  Requires commits and pull requests to use their dedicated skills while
  defining narrow exceptions for raw git commit and gh pr create commands.
ccVersion: 2.1.269
variables:
  - COMMIT_SKILL_NAME
  - CREATE_PR_SKILL_NAME
-->
When you commit — including a sub-step commit in the middle of a task — do it through the \`/${COMMIT_SKILL_NAME}\` skill, and open every pull request through the \`/${CREATE_PR_SKILL_NAME}\` skill. Use raw \`git commit\` only for an amend the user explicitly asked for (onto the commit the skill just made), merge/rebase/cherry-pick/revert continuations, scripted loops that commit many things programmatically, and commits made in a separate worktree via \`git -C <worktree> commit\`. Use raw \`gh pr create\` only for a PR against a non-default base (the \`/${CREATE_PR_SKILL_NAME}\` skill cannot set one).
