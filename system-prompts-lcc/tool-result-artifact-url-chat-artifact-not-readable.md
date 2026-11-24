<!--
name: 'Tool Result: Artifact URL is a claude.ai chat artifact'
description: >-
  Artifact tool's URL-validation error explaining that a link is a
  claude.ai-chat artifact (not one published via this tool), so it cannot be
  read, and to paste the content or save it to a file
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_ARTIFACT_URL_CHAT_ARTIFACT_NOT_READABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_URL_CHAT_ARTIFACT_NOT_READABLE_VAR_1
  - TOOL_RESULT_ARTIFACT_URL_CHAT_ARTIFACT_NOT_READABLE_VAR_2
-->
${TOOL_RESULT_ARTIFACT_URL_CHAT_ARTIFACT_NOT_READABLE_VAR_0} that is an artifact from a claude.ai chat (the chat's artifact panel or its public page), which is separate from artifacts published with this tool and has no ${TOOL_RESULT_ARTIFACT_URL_CHAT_ARTIFACT_NOT_READABLE_VAR_1()} link, so this tool cannot read it. If the user wants its content used here, ask them to paste it or save it to a file in this session; if they meant one of their published artifacts, action: "list" shows those.${TOOL_RESULT_ARTIFACT_URL_CHAT_ARTIFACT_NOT_READABLE_VAR_2}
