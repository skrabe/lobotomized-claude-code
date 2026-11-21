<!--
name: '/login: Named Profile Sign-In Unused'
description: >-
  Message after /login saying the profile problem means this session won't use
  the new sign-in, and how to unset ANTHROPIC_PROFILE.
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_LOGIN_NAMED_PROFILE_SIGN_IN_UNUSED_VAR_0
  - SLASH_COMMAND_LOGIN_NAMED_PROFILE_SIGN_IN_UNUSED_VAR_1
-->
${SLASH_COMMAND_LOGIN_NAMED_PROFILE_SIGN_IN_UNUSED_VAR_0}, so this session won't use the sign-in and Claude Code won't send your prompts. To use the sign-in, unset ANTHROPIC_PROFILE ${SLASH_COMMAND_LOGIN_NAMED_PROFILE_SIGN_IN_UNUSED_VAR_1}, then restart Claude Code.
