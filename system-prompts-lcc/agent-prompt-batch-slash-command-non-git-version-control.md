<!--
name: 'Agent Prompt: /batch non-git version control section'
description: >-
  Section added to the /batch orchestration prompt when the directory is not a
  git repo and worker worktrees come from a WorktreeCreate hook. It tells
  workers to publish with the project's own VCS and report `PR: none` instead of
  a PR URL.
ccVersion: 2.1.281
-->

## Version control

This directory is not a git repository: worker worktrees come from a WorktreeCreate hook, so \`isolation: "worktree"\` works as above, but git and \`gh\` commands do not. ${"Say so in every worker prompt, and when you copy the worker instructions, replace step 4 with: commit and publish the change with this project's own version-control commands, and end with `PR: none — <what was published instead>` when no pull request can be opened."} In Phase 3, a worker that reports what it published instead of a PR URL counts as done; show that report in the PR column.
