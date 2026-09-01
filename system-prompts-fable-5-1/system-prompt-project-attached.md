<!--
name: Project attached header
description: Header line of the Projects context injected into the system prompt.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_PROJECT_ATTACHED_VAR_0
  - SYSTEM_PROMPT_PROJECT_ATTACHED_VAR_1
-->
This session is attached to the Project **"${SYSTEM_PROMPT_PROJECT_ATTACHED_VAR_0(SYSTEM_PROMPT_PROJECT_ATTACHED_VAR_1.name)}"**.
