<!--
name: Synced Memory Mass Delete Held
description: >-
  Bash validateInput error telling the model a command would delete more synced
  memory files than memory sync will allow at once.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_0
  - TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_1
  - TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_2
  - TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_3
-->
This would remove ${TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_0+TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_1} synced memory files at once (${TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_0} already missing, ${TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_1} named here), so nothing was removed. Memory sync holds deletions when more than ${TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_2} synced files are missing at the same time, and restores them all. ${TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_3>0?`Remove at most ${TOOL_RESULT_BASH_SYNCED_MEMORY_MASS_DELETE_HELD_VAR_3} now, wait`:"Wait"} about a minute for memory sync to apply the pending deletions, then continue.
