<!--
name: /list-agents self - main session token
description: >-
  Line in the /list-agents output naming this process's main session token for
  other sessions, shown when the caller is a subagent.
ccVersion: 2.1.239
variables:
  - SLASH_COMMAND_LIST_AGENTS_SELF_MAIN_SESSION_TOKEN_VAR_0
  - SLASH_COMMAND_LIST_AGENTS_SELF_MAIN_SESSION_TOKEN_VAR_1
-->
This process's main session: ${SLASH_COMMAND_LIST_AGENTS_SELF_MAIN_SESSION_TOKEN_VAR_0.self.token} (the name OTHER sessions use for it; from inside this process, address it as "${SLASH_COMMAND_LIST_AGENTS_SELF_MAIN_SESSION_TOKEN_VAR_1}")
