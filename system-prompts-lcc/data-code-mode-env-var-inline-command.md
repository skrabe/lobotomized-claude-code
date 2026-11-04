<!--
name: 'Data: Code Mode env var inline command'
description: >-
  Inline VAR=value claude command form for setting the Code Mode variable on
  non-Windows shells
ccVersion: 2.1.318
variables:
  - DATA_CODE_MODE_ENV_VAR_INLINE_COMMAND_VAR_0
  - DATA_CODE_MODE_ENV_VAR_INLINE_COMMAND_VAR_1
  - DATA_CODE_MODE_ENV_VAR_INLINE_COMMAND_VAR_2
  - DATA_CODE_MODE_ENV_VAR_INLINE_COMMAND_VAR_3
-->
${DATA_CODE_MODE_ENV_VAR_INLINE_COMMAND_VAR_0==="step"?"run ":""}${DATA_CODE_MODE_ENV_VAR_INLINE_COMMAND_VAR_1}=${DATA_CODE_MODE_ENV_VAR_INLINE_COMMAND_VAR_2} ${DATA_CODE_MODE_ENV_VAR_INLINE_COMMAND_VAR_3}
