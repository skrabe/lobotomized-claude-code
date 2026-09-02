<!--
name: 'System Prompt: Memory scope privacy defaults'
description: >-
  Same emission site and rendered text as the 2.1.221 id (the first sentence was
  factored out into the Ayo() helper): per-type privacy defaults plus the
  no-secrets-in-team rule.
ccVersion: 2.1.224
variables:
  - SYSTEM_PROMPT_MEMORY_SCOPE_PRIVACY_DEFAULTS_VAR_0
-->
 ${SYSTEM_PROMPT_MEMORY_SCOPE_PRIVACY_DEFAULTS_VAR_0("team")} Never write secrets or credentials to the team directory.
