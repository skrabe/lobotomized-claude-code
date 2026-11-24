<!--
name: 'Steward: git watch ended'
description: >-
  Prompt saying a git-only watch has ended, with the reason; change nothing and
  tell the user why, where the branch stood, and what is open.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_0
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_1
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_3
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_4
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_5
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_6
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_8
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_9
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_10
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_11
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_12
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_13
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_14
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_15
  - SKILL_STEWARD_GIT_WATCH_ENDED_VAR_16
-->
# /${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_0}: the watch of ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_1} has ended

${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.kind==="closed"?SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.isHostsWord?`Its ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_3(SKILL_STEWARD_GIT_WATCH_ENDED_VAR_4.host)} was ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.state==="merged"?"merged":"closed without a merge"}.`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.state==="closed"?`${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_1} is gone from ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_5}.`:`${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_1} adds nothing to ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_6} any more: it was merged, or its changes got there another way.`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.passesWithNoLook!==void 0?`For ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.passesWithNoLook} passes in a row Claude Code's own looks between them couldn't tell whether anything had changed, so each pass cost a turn. Most likely git can't reach the remote: tell the user that \`git ls-remote ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_5}\` shows why.`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.timeIsUp?`It has reached its time limit (${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.days} days at most).`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.bypass!==void 0?`Nothing would ask before a command now: ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.bypass}.`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.isOff||SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.isPlanning?SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.isOff?`/${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_0} has been turned off.`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_8:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.denied!==void 0?`It can't go on: ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.denied}.`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.notReached!==void 0?`${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.notReached}.`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.notHeld!==void 0?`Claude Code can no longer hold it to this branch: ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.notHeld}.`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.kind==="not_yours"?`It can't be looked after from here any more: ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.why}.`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.isNotYet?`${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.unreadLooks} wake-ups in a row couldn't check what the last merge of the base changed. That merge may still be open in the checkout: tell the user that \`git status\` shows it.`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.kind==="unknown"?`${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_7.unreadLooks} wake-ups in a row couldn't read it: ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.say}.`:`This session's folder is no longer a checkout of ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_9}.`} The wake-up is cancelled already.

Change nothing: no edit, no commit, no push. Then ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_10({briefMode:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_11()})}: why the watch ended, where the branch stood when you last looked, and what is still open.${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_12&&SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.kind==="yours"||!SKILL_STEWARD_GIT_WATCH_ENDED_VAR_13&&SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.kind==="unknown"&&(SKILL_STEWARD_GIT_WATCH_ENDED_VAR_4.host&&SKILL_STEWARD_GIT_WATCH_ENDED_VAR_14(SKILL_STEWARD_GIT_WATCH_ENDED_VAR_4.host))!=="new_each_time"?` End with: "Run /${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_0} ${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_15(SKILL_STEWARD_GIT_WATCH_ENDED_VAR_4)} to keep watching."`:SKILL_STEWARD_GIT_WATCH_ENDED_VAR_2.kind==="closed"?" There is nothing left to watch, so don't offer to start again.":""}${SKILL_STEWARD_GIT_WATCH_ENDED_VAR_16()}
