<!--
name: 'Tool Result: Send-to-project default environment'
description: Reports the new project uses the organization default cloud environment
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_DEFAULT_ENVIRONMENT_VAR_0
-->
${TOOL_RESULT_SEND_TO_PROJECT_DEFAULT_ENVIRONMENT_VAR_0.environmentLookupFailed?"Your cloud environments couldn’t be looked up":"No cloud environment is set"}, so the project uses your organization’s default. Pick one in project settings if its threads do not start.
