<!--
name: User deny-rules permission context
description: >-
  Injected permission context describing the user's configured deny rules for
  the safety judge.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_USER_DENY_RULES_VAR_0
  - SYSTEM_PROMPT_USER_DENY_RULES_VAR_1
-->
- User Deny Rules: The user has configured these permission deny rules: ${SYSTEM_PROMPT_USER_DENY_RULES_VAR_0.map((SYSTEM_PROMPT_USER_DENY_RULES_VAR_1)=>`\`${SYSTEM_PROMPT_USER_DENY_RULES_VAR_1}\``).join(", ")}. Each rule names a tool and (optionally) an argument pattern that is already hard-blocked for that tool. 
