<!--
name: 'Tool Result: Remote tool keychain query refused'
description: >-
  Refuses a cloud-session command that queries the credential store, explaining
  why and suggesting simpler commands
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_TOOL_KEYCHAIN_QUERY_REFUSED_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_KEYCHAIN_QUERY_REFUSED_VAR_1
-->
${TOOL_RESULT_REMOTE_TOOL_KEYCHAIN_QUERY_REFUSED_VAR_0} does not let a cloud session query its credential store (\`${TOOL_RESULT_REMOTE_TOOL_KEYCHAIN_QUERY_REFUSED_VAR_1}\`). Nothing was run. Either the command names one of the store's tools or APIs, or it has more quoting or escaping than could be checked for such a name; if it names none, split it into simpler commands.
