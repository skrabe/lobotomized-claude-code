<!--
name: 'Slash command: Steward terms programs run with credentials (any forge)'
description: >-
  Warns that programs and aliases can still push or merge with the user's
  credentials
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_ANY_FORGE_VAR_0
  - SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_ANY_FORGE_VAR_1
-->
- Programs I run, like tests, can still force-push or merge the request with your credentials. So can a shell alias or function of yours that runs git, glab or the like under another name, such as g for git. Only this session's permission mode covers them, and every other command I run: here, ${SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_ANY_FORGE_VAR_0.guard}.${SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_ANY_FORGE_VAR_0.unprompted&&` But ${SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_ANY_FORGE_VAR_0.unprompted} run unasked.`}${SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_ANY_FORGE_VAR_0.unasked===void 0?"":` ${SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_ANY_FORGE_VAR_1(SLASH_COMMAND_PR_STEWARD_TERMS_PROGRAMS_RUN_WITH_CREDENTIALS_ANY_FORGE_VAR_0.unasked)}`}
