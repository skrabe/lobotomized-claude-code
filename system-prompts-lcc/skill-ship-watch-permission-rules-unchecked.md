<!--
name: 'Ship: Watch Permission Rules Unchecked'
description: >-
  Reason in the /ship watch-start report, returned as Cs().why, saying this
  session's permission rules couldn't be checked and telling the user to run the
  watch again (or after this review).
ccVersion: 2.1.330
variables:
  - SKILL_SHIP_WATCH_PERMISSION_RULES_UNCHECKED_VAR_0
  - SKILL_SHIP_WATCH_PERMISSION_RULES_UNCHECKED_VAR_1
-->
this session's permission rules couldn't be checked. ${SKILL_SHIP_WATCH_PERMISSION_RULES_UNCHECKED_VAR_0?`After this review, run /${SKILL_SHIP_WATCH_PERMISSION_RULES_UNCHECKED_VAR_1} to watch`:`Run /${SKILL_SHIP_WATCH_PERMISSION_RULES_UNCHECKED_VAR_1} again`}
