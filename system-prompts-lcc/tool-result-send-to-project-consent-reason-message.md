<!--
name: 'Tool result: Send to project consent reason (message run)'
description: >-
  Permission decisionReason for a message-sending run, stating what is posted
  with the user's Claude account plus the transcript disclosure lines.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_MESSAGE_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_MESSAGE_VAR_1
  - TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_MESSAGE_VAR_2
-->
${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_MESSAGE_VAR_0.project_id!==void 0?`With your Claude account, this message is posted in ${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_MESSAGE_VAR_1}.`:"With your Claude account, a Claude Project is created and this message is posted in it. This repository’s GitHub origin may be added to it."} ${TOOL_RESULT_SEND_TO_PROJECT_CONSENT_REASON_MESSAGE_VAR_2.join(" ")}
