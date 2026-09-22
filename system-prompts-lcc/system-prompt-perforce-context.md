<!--
name: Perforce workspace context
description: Perforce-workspace note injected into the system prompt's environment context.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_PERFORCE_CONTEXT_VAR_0
  - SYSTEM_PROMPT_PERFORCE_CONTEXT_VAR_1
  - SYSTEM_PROMPT_PERFORCE_CONTEXT_VAR_2
-->
This is a Perforce workspace. Files not yet opened for edit are read-only; if a file is read-only, run \`p4 edit <file>\` via ${SYSTEM_PROMPT_PERFORCE_CONTEXT_VAR_0()?SYSTEM_PROMPT_PERFORCE_CONTEXT_VAR_1:SYSTEM_PROMPT_PERFORCE_CONTEXT_VAR_2} to check it out before modifying. Files that are already writable have been opened and can be edited directly.
