<!--
name: 'Skill: Steward watch still on, type stop'
description: >-
  Says the watch is still on and can only be ended by typing the stop command at
  this session's own prompt (Esc also, when available).
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_WATCH_STILL_ON_TYPE_STOP_VAR_0
  - SKILL_STEWARD_WATCH_STILL_ON_TYPE_STOP_VAR_1
  - SKILL_STEWARD_WATCH_STILL_ON_TYPE_STOP_VAR_2
-->
The watch is still on. To end it, type ${SKILL_STEWARD_WATCH_STILL_ON_TYPE_STOP_VAR_0} yourself at this session's own prompt, on the computer that runs it. It doesn't count from Claude, another device, or a program.${SKILL_STEWARD_WATCH_STILL_ON_TYPE_STOP_VAR_1()&&SKILL_STEWARD_WATCH_STILL_ON_TYPE_STOP_VAR_2()?" Esc ends the watch too.":""}
