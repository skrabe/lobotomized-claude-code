<!--
name: Project synced-source overflow
description: >-
  Overflow notice on the Project docs/files/synced-sources/memory lists,
  directing the model to the named Projects method (project_info) for the full
  list.
ccVersion: 2.1.325
variables:
  - SYSTEM_PROMPT_PROJECT_AND_MORE_CALL_PROJECT_INFO_FOR_VAR_0
  - SYSTEM_PROMPT_PROJECT_AND_MORE_CALL_PROJECT_INFO_FOR_VAR_1
-->

- … and ${SYSTEM_PROMPT_PROJECT_AND_MORE_CALL_PROJECT_INFO_FOR_VAR_0} more${SYSTEM_PROMPT_PROJECT_AND_MORE_CALL_PROJECT_INFO_FOR_VAR_1===void 0?"":` — call \`${SYSTEM_PROMPT_PROJECT_AND_MORE_CALL_PROJECT_INFO_FOR_VAR_1}\` for the full list`}
