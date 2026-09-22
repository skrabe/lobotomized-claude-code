<!--
name: 'Tool Description: Memory version token requirement'
description: >-
  Version-tokens section of the memory_write prompt telling the model every
  write needs if_version and never to invent a token.
ccVersion: 2.1.224
variables:
  - TOOL_DESCRIPTION_MEMORY_VERSION_TOKEN_REQUIREMENT_VAR_0
  - TOOL_DESCRIPTION_MEMORY_VERSION_TOKEN_REQUIREMENT_VAR_1
-->
Every ${TOOL_DESCRIPTION_MEMORY_VERSION_TOKEN_REQUIREMENT_VAR_0} needs if_version. Pass the literal word new for a document that does not yet exist. For a document that already exists, ${TOOL_DESCRIPTION_MEMORY_VERSION_TOKEN_REQUIREMENT_VAR_1} it first and pass the version token from that result — the listing shows paths, not tokens. Never invent a token.
