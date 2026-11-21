<!--
name: 'Tool result: connector download offer summary'
description: >-
  Summary of files a connector offered, listed by index and name, in the tool
  result.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_0
  - TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_1
  - TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_2
-->
The connector offered ${TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_0===1?"1 file":`${TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_0} files`}${TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_0>TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_1.length?`, of which the first ${TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_1.length} are listed here`:""}: ${TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_1.join(", ")}.${TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_2.length>TOOL_RESULT_CONNECTOR_DOWNLOAD_OFFER_SUMMARY_VAR_1.length?" For the names of any later files that were saved, list the folder that the notes give.":""}
