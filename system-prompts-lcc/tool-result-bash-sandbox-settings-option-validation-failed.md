<!--
name: 'Tool result: Bash sandbox settings option validation failed'
description: >-
  Reason the sandbox is unavailable when sandbox settings passed via --settings
  or the SDK settings option fail validation
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BASH_SANDBOX_SETTINGS_OPTION_VALIDATION_FAILED_VAR_0
  - TOOL_RESULT_BASH_SANDBOX_SETTINGS_OPTION_VALIDATION_FAILED_VAR_1
-->
the settings passed with --settings or the SDK's settings option configure the sandbox but failed validation, so none of them apply${TOOL_RESULT_BASH_SANDBOX_SETTINGS_OPTION_VALIDATION_FAILED_VAR_0.firstError?` (${TOOL_RESULT_BASH_SANDBOX_SETTINGS_OPTION_VALIDATION_FAILED_VAR_1(TOOL_RESULT_BASH_SANDBOX_SETTINGS_OPTION_VALIDATION_FAILED_VAR_0.firstError,{maxCodeUnits:300})})`:""}. Fix them and start again
