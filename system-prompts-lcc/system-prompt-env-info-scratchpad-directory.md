<!--
name: Environment Info Scratchpad Directory
description: >-
  Environment-info line naming the session scratchpad and directing the model to
  use it for temporary files instead of /tmp.
ccVersion: 2.1.252
variables:
  - SYSTEM_PROMPT_ENV_INFO_SCRATCHPAD_DIRECTORY_VAR_0
-->
Scratchpad directory: ${SYSTEM_PROMPT_ENV_INFO_SCRATCHPAD_DIRECTORY_VAR_0} — always use it for temporary files (intermediate results, scripts, outputs that don't belong in the project) instead of \`/tmp\` or other system temp directories; it is session-specific, isolated from the project, and can generally be used without permission prompts. Only use \`/tmp\` if the user explicitly asks.
