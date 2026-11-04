<!--
name: 'Agent prompt: auto mode REPL batched script header'
description: >-
  Comment header labelling each script when several unchecked REPL scripts are
  sent together to auto mode's classifier
ccVersion: 2.1.318
variables:
  - AGENT_PROMPT_AUTO_MODE_REPL_BATCHED_SCRIPT_HEADER_VAR_0
  - AGENT_PROMPT_AUTO_MODE_REPL_BATCHED_SCRIPT_HEADER_VAR_1
  - AGENT_PROMPT_AUTO_MODE_REPL_BATCHED_SCRIPT_HEADER_VAR_2
  - AGENT_PROMPT_AUTO_MODE_REPL_BATCHED_SCRIPT_HEADER_VAR_3
-->
// [${AGENT_PROMPT_AUTO_MODE_REPL_BATCHED_SCRIPT_HEADER_VAR_0}] Script ${AGENT_PROMPT_AUTO_MODE_REPL_BATCHED_SCRIPT_HEADER_VAR_1+1} of ${AGENT_PROMPT_AUTO_MODE_REPL_BATCHED_SCRIPT_HEADER_VAR_2.length}; these scripts started in this order in one REPL
${AGENT_PROMPT_AUTO_MODE_REPL_BATCHED_SCRIPT_HEADER_VAR_3.code}
