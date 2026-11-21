<!--
name: 'Skill: Steward hosted agent take-over notice'
description: >-
  Explains that a hosted agent already drives the pull request, how the user can
  take over, and that no local watch runs meanwhile
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_HOSTED_AGENT_TAKE_OVER_NOTICE_VAR_0
  - SKILL_STEWARD_HOSTED_AGENT_TAKE_OVER_NOTICE_VAR_1
  - SKILL_STEWARD_HOSTED_AGENT_TAKE_OVER_NOTICE_VAR_2
-->
${SKILL_STEWARD_HOSTED_AGENT_TAKE_OVER_NOTICE_VAR_0.atAStart}. To take over, ${SKILL_STEWARD_HOSTED_AGENT_TAKE_OVER_NOTICE_VAR_0.takeOver}, since it may have pushed, then run ${SKILL_STEWARD_HOSTED_AGENT_TAKE_OVER_NOTICE_VAR_1} again.${SKILL_STEWARD_HOSTED_AGENT_TAKE_OVER_NOTICE_VAR_2?" If git says that uncommitted edits, yours or my review's, are in the pull's way, run git stash -u first: git stash pop brings them back.":""} In the meantime I won't watch it from here, so that two agents don't push to one branch${SKILL_STEWARD_HOSTED_AGENT_TAKE_OVER_NOTICE_VAR_2?": I only review":""}.
