<!--
name: 'Skill: Steward branch waiting and stopping'
description: >-
  Explains automatic wake-ups for a git-only branch watch, when it ends, and how
  to stop and report the branch's status
ccVersion: 2.1.332
variables:
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_0
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_1
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_2
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_3
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_4
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_5
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_7
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_8
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_9
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_10
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_11
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_12
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_13
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_14
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_15
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_16
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_17
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_18
  - SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_19
-->
## Waiting

A turn that ends without a wake-up ends the watch, but for the one that waits for a background review. So at the end of each pass, unless you are stopping (the start's hand-over has its own delay):
${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_0?`1. First ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_1}
2. Then, as the last action of the turn, ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_2}`:`1. First ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_2}
2. Then ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_1}`}

Between your passes Claude Code asks the remote by itself, every two minutes. Once \`${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_3}\` and \`${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_4}\` conflict, somebody else pushes to \`${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_3}\`, ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_5(SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6.host).checks?"a check turns red or green, ":""}${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_5(SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6.host).words&&SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6.host?.SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_7.SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_8===void 0?"somebody whose words count writes, ":""}${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_5(SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6.host).end&&SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6.host?.SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_9.SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_8===void 0?`the ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_10(SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6.host)} is merged or closed, `:""}or \`${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_3}\` is gone or adds nothing any more, it wakes you within a few minutes, whatever delay you gave, though no sooner than ten minutes after it last woke you. Otherwise it puts your wake-up off, so that a quiet watch costs the user no turn. A base that merely moves is no news. Start no wait or poll of your own.

**A turn that a task notification begins** (the review's findings) changes nothing: no edit, no commit, no push. Unless you have stopped, or the user has pressed Esc or started a /loop since, call ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_11} with the same \`prompt\` and \`delaySeconds: ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_12}\`, and end the turn. The pass that it starts does the work, under these rules.

## Stopping

Claude Code ends the watch by itself once \`${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_3}\` is gone from \`${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_13}\` or adds nothing to \`${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_4}\` any more, ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_5(SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6.host).end?`its ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_10(SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6.host)} is merged, closed or aimed at another branch, `:""}another branch is checked out, the session goes into bypass mode or plan mode or loses the fence, or ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_14} days are over. Stop it yourself when the user says stop.${!SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_5(SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6.host).words?"":` Or when somebody whose words Claude Code kept asks on the ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_10(SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6.host)} that you stop, hold off or leave the branch alone, or says that they are handling it: push nothing more, and tell the user who asked.`}

To stop: call ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_11} with \`stop: true\` and nothing else, then ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_15({briefMode:SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_16()})}: where the branch stands, what is still open, why you stopped, and "Run /${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_17} ${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_18(SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_6)} to keep watching."${SKILL_STEWARD_BRANCH_WAITING_AND_STOPPING_VAR_19()}
