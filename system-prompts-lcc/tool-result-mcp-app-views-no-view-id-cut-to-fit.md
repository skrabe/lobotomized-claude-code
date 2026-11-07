<!--
name: 'Tool Result: MCP app views without widget_id cut to fit'
description: >-
  Explains that views without a widget_id cannot be read alone, so their shared
  state was cut to fit and marked cut_for_size
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_APP_VIEWS_NO_VIEW_ID_CUT_TO_FIT_VAR_0
-->
${TOOL_RESULT_MCP_APP_VIEWS_NO_VIEW_ID_CUT_TO_FIT_VAR_0===1?"1 view has":`${TOOL_RESULT_MCP_APP_VIEWS_NO_VIEW_ID_CUT_TO_FIT_VAR_0} views have`} no widget_id, so ${TOOL_RESULT_MCP_APP_VIEWS_NO_VIEW_ID_CUT_TO_FIT_VAR_0===1?"it":"they"} cannot be read alone: what ${TOOL_RESULT_MCP_APP_VIEWS_NO_VIEW_ID_CUT_TO_FIT_VAR_0===1?"it":"each"} shared was cut to fit, and "cut_for_size" marks ${TOOL_RESULT_MCP_APP_VIEWS_NO_VIEW_ID_CUT_TO_FIT_VAR_0===1?"it":"them"} inside the tag above. 
