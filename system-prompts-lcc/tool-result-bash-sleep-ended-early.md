<!--
name: 'Tool result: Bash sleep ended early'
description: >-
  Bash output note that a sleep ended early because the agents or background
  programs beside it finished
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_0
  - TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_1
  - TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_2
  - TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_3
  - TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_4
-->
[The sleep ended early, after ${TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_0.round(TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_1)} s of ${TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_0.round(TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_2)} s, because ${TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_3?"the agents and any background programs that ran beside it have ended":"the background programs that ran beside it have exited"}.${TOOL_RESULT_BASH_SLEEP_ENDED_EARLY_VAR_4.size>0?" Programs that listen on a port, and the scripts that started them, were not waited for and may still run.":""}]
