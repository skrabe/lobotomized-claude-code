<!--
name: 'Slash command: PR Steward terms programs use credentials'
description: >-
  Warns that programs such as tests can still merge or force-push and only the
  permission mode covers them
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_VAR_0
  - SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_VAR_1
  - SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_VAR_2
  - SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_VAR_3
-->
- Programs I run, like tests, can still merge or force-push with your credentials. So can a shell alias or function of yours that runs gh or git under another name, such as g for git. Only this session's permission mode covers them, and every other command I run: here, ${SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_VAR_0}.${SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_VAR_1&&` But ${SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_VAR_1} run unasked.`}${SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_VAR_2===void 0?"":` ${SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_VAR_3(SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_VAR_2)}`}
