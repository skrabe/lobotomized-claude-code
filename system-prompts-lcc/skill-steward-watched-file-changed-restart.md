<!--
name: 'Skill: Steward watched file changed'
description: >-
  Names a file that changed after the watch started and tells how to restart
  after review
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_WATCHED_FILE_CHANGED_RESTART_VAR_0
  - SKILL_STEWARD_WATCHED_FILE_CHANGED_RESTART_VAR_1
  - SKILL_STEWARD_WATCHED_FILE_CHANGED_RESTART_VAR_2
  - SKILL_STEWARD_WATCHED_FILE_CHANGED_RESTART_VAR_3
-->
${SKILL_STEWARD_WATCHED_FILE_CHANGED_RESTART_VAR_0.changed} changed after /${SKILL_STEWARD_WATCHED_FILE_CHANGED_RESTART_VAR_1} started, and gh, git, or /${SKILL_STEWARD_WATCHED_FILE_CHANGED_RESTART_VAR_1} relies on it. Once the user has reviewed the change, they can run /${SKILL_STEWARD_WATCHED_FILE_CHANGED_RESTART_VAR_1} ${SKILL_STEWARD_WATCHED_FILE_CHANGED_RESTART_VAR_2(SKILL_STEWARD_WATCHED_FILE_CHANGED_RESTART_VAR_3)} to start again
