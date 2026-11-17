<!--
name: 'Tool Description: Bash (PR Steward labels)'
description: >-
  PR Steward labels guidance (NBt) appended to the /loop autonomous preamble,
  the /loop skill prompt and the autofix-pr session prompt: check a PR's labels
  before pushing or starting a babysit/monitor loop, and what options to offer
  the user if PR Steward already has the PR
ccVersion: 2.1.326
variables:
  - TOOL_DESCRIPTION_BASH_PR_STEWARD_LABELS_GUIDANCE_VAR_0
  - TOOL_DESCRIPTION_BASH_PR_STEWARD_LABELS_GUIDANCE_VAR_1
  - TOOL_DESCRIPTION_BASH_PR_STEWARD_LABELS_GUIDANCE_VAR_2
-->
## PR Steward

PR Steward is a Claude agent that can watch a GitHub pull request, fix its CI and work through its review comments. It puts the \`${TOOL_DESCRIPTION_BASH_PR_STEWARD_LABELS_GUIDANCE_VAR_0}\` label on a PR it is watching, and adds \`${TOOL_DESCRIPTION_BASH_PR_STEWARD_LABELS_GUIDANCE_VAR_1}\` while it is making a change. A second agent pushing to the same PR races it: one pushes, then the other rebases over it.

Before you push to a PR, or start babysitting or monitoring one, check its labels (\`gh pr view <number> -R <owner>/<repo> --json labels\`). If either label is on the PR, do not push and do not start a babysit or monitor loop for it, even one you were asked to start, until the user picks one of these choices. Tell the user PR Steward has this PR and offer:

1. Leave it with PR Steward: report the PR's status and change nothing.
2. Make this one change and hand back: make only that change. While \`${TOOL_DESCRIPTION_BASH_PR_STEWARD_LABELS_GUIDANCE_VAR_1}\` is on the PR, Steward is in the middle of a change, so wait for the label to clear or warn the user and get their go-ahead. Pull the latest branch before touching anything.
3. Take over: PR Steward stands down when a person removes \`${TOOL_DESCRIPTION_BASH_PR_STEWARD_LABELS_GUIDANCE_VAR_0}\`, which also archives its session. ${TOOL_DESCRIPTION_BASH_PR_STEWARD_LABELS_GUIDANCE_VAR_2}

If only \`${TOOL_DESCRIPTION_BASH_PR_STEWARD_LABELS_GUIDANCE_VAR_1}\` is on the PR, PR Steward may have stopped without clearing it; say so, and that the user can remove it if PR Steward is not active.

If the user is away (a loop tick or a scheduled run), do not choose for them: report once that PR Steward has the PR, not on every tick, and leave the PR alone.
