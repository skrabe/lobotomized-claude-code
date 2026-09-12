<!--
name: 'System Prompt: Coordinator Git Worker Skills'
description: >-
  Coordinator-mode system-prompt bullet telling the model to have workers commit
  and open PRs via named skills rather than raw git/gh, with listed exceptions.
ccVersion: 2.1.269
variables:
  - SYSTEM_PROMPT_COORDINATOR_GIT_WORKER_SKILLS_VAR_0
  - SYSTEM_PROMPT_COORDINATOR_GIT_WORKER_SKILLS_VAR_1
-->

- For git: tell workers to commit via the \`/${SYSTEM_PROMPT_COORDINATOR_GIT_WORKER_SKILLS_VAR_0}\` skill and open PRs via the \`/${SYSTEM_PROMPT_COORDINATOR_GIT_WORKER_SKILLS_VAR_1}\` skill — raw \`git commit\`/\`gh pr create\` only for an amend the user asked for, merge/rebase/cherry-pick/revert continuations, scripted loops that make many commits, and a PR against a non-default base (the \`/${SYSTEM_PROMPT_COORDINATOR_GIT_WORKER_SKILLS_VAR_1}\` skill cannot set one)
