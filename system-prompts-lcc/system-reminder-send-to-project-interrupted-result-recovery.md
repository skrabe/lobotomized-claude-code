<!--
name: 'System Reminder: Send-to-project interrupted result recovery'
description: >-
  Reports the committed project-transfer result after interruption and explains
  when rerunning could duplicate a project or setup card
ccVersion: 2.1.314
variables:
  - ESCAPE_TOOL_RESULT_TEXT_FN
  - TOOL_RESULT_BLOCK
  - PROJECT_TRANSFER_OUTCOME
  - HAS_CONFIRMED_DELIVERY
  - HAS_CONFIRMED_OR_UNCERTAIN_DELIVERY
-->
${ESCAPE_TOOL_RESULT_TEXT_FN(typeof TOOL_RESULT_BLOCK.content==="string"?TOOL_RESULT_BLOCK.content:PROJECT_TRANSFER_OUTCOME.result.projectUrl)}
${PROJECT_TRANSFER_OUTCOME.result.mode==="existing"?HAS_CONFIRMED_DELIVERY?"Tell the user what landed (above).":HAS_CONFIRMED_OR_UNCERTAIN_DELIVERY?"Tell the user what is said above.":"Nothing reached the project; tell the user and offer to run /send-to-project again.":PROJECT_TRANSFER_OUTCOME.result.message==="not_sent"?"Tell the user what is said above. A new run must pick this project, or it makes a second one.":"Do not run /send-to-project again for this folder unless the user wants a second project."}${PROJECT_TRANSFER_OUTCOME.result.setupUncertain?" The setup card may or may not have been posted: ask the user to check the project before they run /send-to-project again.":""}
