<!--
name: Utility JSON retry prompt
description: >-
  User-turn retry message in a utility model call demanding a valid JSON-only
  response.
ccVersion: 2.1.206
variables:
  - DATA_UTILITY_JSON_RETRY_VAR_0
-->
${DATA_UTILITY_JSON_RETRY_VAR_0}

Previous response was not valid JSON. Respond with ONLY the JSON object, nothing else.
