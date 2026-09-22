<!--
name: NL date/time parser — user context template
description: >-
  The user-message content (current date/timezone plus the user's input) sent to
  the datetime-parser model.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_NL_DATETIME_PARSER_USER_CONTEXT_VAR_0
  - SYSTEM_PROMPT_NL_DATETIME_PARSER_USER_CONTEXT_VAR_1
  - SYSTEM_PROMPT_NL_DATETIME_PARSER_USER_CONTEXT_VAR_2
  - SYSTEM_PROMPT_NL_DATETIME_PARSER_USER_CONTEXT_VAR_3
  - SYSTEM_PROMPT_NL_DATETIME_PARSER_USER_CONTEXT_VAR_4
-->
Current context:
- Current date and time: ${SYSTEM_PROMPT_NL_DATETIME_PARSER_USER_CONTEXT_VAR_0} (UTC)
- Local timezone: ${SYSTEM_PROMPT_NL_DATETIME_PARSER_USER_CONTEXT_VAR_1}
- Day of week: ${SYSTEM_PROMPT_NL_DATETIME_PARSER_USER_CONTEXT_VAR_2}

User input: "${SYSTEM_PROMPT_NL_DATETIME_PARSER_USER_CONTEXT_VAR_3}"

Output format: ${SYSTEM_PROMPT_NL_DATETIME_PARSER_USER_CONTEXT_VAR_4}

Parse the user's input into ISO 8601 format. Return ONLY the formatted string, or "INVALID" if the input is incomplete or unparseable.
