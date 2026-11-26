<!--
name: 'Skill: Steward git arm wake-up call'
description: >-
  How to call the wake-up tool with prompt, reason, noop and delay for a git
  watch pass
ccVersion: 2.1.332
variables:
  - SKILL_STEWARD_GIT_ARM_WAKEUP_CALL_VAR_0
  - SKILL_STEWARD_GIT_ARM_WAKEUP_CALL_VAR_1
  - SKILL_STEWARD_GIT_ARM_WAKEUP_CALL_VAR_2
  - SKILL_STEWARD_GIT_ARM_WAKEUP_CALL_VAR_3
  - SKILL_STEWARD_GIT_ARM_WAKEUP_CALL_VAR_4
-->
call ${SKILL_STEWARD_GIT_ARM_WAKEUP_CALL_VAR_0} with \`prompt\` exactly \`${SKILL_STEWARD_GIT_ARM_WAKEUP_CALL_VAR_1(SKILL_STEWARD_GIT_ARM_WAKEUP_CALL_VAR_2)}\`, a one-sentence \`reason\`, \`noop: true\` only if this pass changed nothing and you have nothing new to tell the user (a pass with \`noop: true\` is folded away on the screen at the next wake-up), and \`delaySeconds: ${SKILL_STEWARD_GIT_ARM_WAKEUP_CALL_VAR_3}\`. If a fetch or a push of this pass failed because the remote didn't answer, give ${SKILL_STEWARD_GIT_ARM_WAKEUP_CALL_VAR_4} instead, to try again in ten minutes.
