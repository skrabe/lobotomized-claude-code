<!--
name: 'Skill: Steward risky file push choice'
description: >-
  Tells the user to push the flagged files explicitly or take them out of the
  unpushed commits, then run again.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_0
  - SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_1
  - SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_2
  - SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_3
  - SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_4
  - SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_5
-->
If ${SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_0} should go up, run ${SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_1}. If not, take ${SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_2} out of ${SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_3?.SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_4.SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_5?`every unpushed commit: a new commit that removes ${SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_2} still leaves ${SKILL_STEWARD_RISKY_FILE_PUSH_CHOICE_VAR_2} in the history`:"your commits"}. Then run
