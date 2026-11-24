<!--
name: 'Steward: start git-only branch watch'
description: >-
  Prompt for starting a git-only /steward watch: show the summary lines,
  optionally review, check the remote, and hand over to the first pass with a
  wake-up.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_0
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_1
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_2
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_3
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_4
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_5
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_6
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_7
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_8
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_9
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_10
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_11
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_12
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_13
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_14
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_15
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_16
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_17
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_18
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_19
  - SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_20
-->
# /${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_0}: ${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_1?`review ${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_2}, then watch it`:`watch ${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_2}`}, with git alone

${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_3?"Claude Code itself has already shown the user these lines. Don't repeat them:":SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_4("lines")}

${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_5(SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_6(SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_3?SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_7:{...SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_7,folds:!1}))}

The full terms of this run${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_3?", which the user can open in that row":""}. They hold as they stand. Print them only if the user asks:

${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_5(SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_8)}

Add a line on any unpushed commits (they go up) and uncommitted changes (they don't): \`${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_9.status}\`.

${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_10(SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_11,SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_11.root,SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_9,SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_7.isTurnSourceKnown,SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_7.stop,SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_12.host!==void 0)}

${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_13()?`## First, try the remote

Run \`${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_9.fetchBase}\`${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_14(SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_15)} now, while the user is here. If the sandbox blocks it (the message speaks of a network or host allowlist), this watch can't work: try no other way, stop as "Stopping" says, and tell the user that Claude Code's sandbox doesn't let git reach ${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_15}, in the message's own terms.

`:""}${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_1?`## 1. Review

${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_7.callReview} TARGET is \`${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_16}...HEAD\`, after \`${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_9.fetchBase}\`${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_14(SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_15)}, so that the review covers the local head and its unpushed commits.

If the tool says that the review runs in the background, say so in one line and end your turn, with no wake-up: the findings begin the next turn.

## 2. Hand over to the first pass

This turn changes nothing: no edit, no commit, no push. Once the findings are back in this turn, call`:`## Hand over to the first pass

This turn changes nothing: no edit, no commit, no push. Call`} ${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_17} with \`prompt\` exactly \`${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_18(SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_12)}\`, a one-sentence \`reason\` and ${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_7.hasWorkNow?`\`delaySeconds: ${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_19.secondsAfterANotification}\`, tell the user that the first check-in starts in a minute, and end the turn. That pass ${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_1?"deals with the findings":"does the work"}.`:`\`delaySeconds: ${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_19.secondsWhileQuiet}\`, tell the user that nothing needs doing now and that you look again when something changes, and end the turn.`}

${SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_20(SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_12,SKILL_STEWARD_START_GIT_BRANCH_WATCH_VAR_19)}
