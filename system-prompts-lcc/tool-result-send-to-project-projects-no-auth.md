<!--
name: 'Send to Project: Projects require Claude.ai login'
description: >-
  Reason appended to an auth detail when Projects requests fail because there is
  no Claude.ai login, pointing to /login.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_PROJECTS_NO_AUTH_VAR_0
-->
${TOOL_RESULT_SEND_TO_PROJECT_PROJECTS_NO_AUTH_VAR_0.detail}. Projects require a Claude.ai login (/login).
