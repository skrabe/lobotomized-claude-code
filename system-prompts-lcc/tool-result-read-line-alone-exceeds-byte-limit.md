<!--
name: 'Read tool error: single line exceeds byte limit'
description: >-
  Error returned by the lightweight read tool (view_range path) when one line
  alone exceeds the byte limit, so narrowing view_range cannot help.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_READ_LINE_ALONE_EXCEEDS_BYTE_LIMIT_VAR_0
  - TOOL_RESULT_READ_LINE_ALONE_EXCEEDS_BYTE_LIMIT_VAR_1
  - TOOL_RESULT_READ_LINE_ALONE_EXCEEDS_BYTE_LIMIT_VAR_2
  - TOOL_RESULT_READ_LINE_ALONE_EXCEEDS_BYTE_LIMIT_VAR_3
-->
read: line ${TOOL_RESULT_READ_LINE_ALONE_EXCEEDS_BYTE_LIMIT_VAR_0(this,TOOL_RESULT_READ_LINE_ALONE_EXCEEDS_BYTE_LIMIT_VAR_1,"f")+1} of ${TOOL_RESULT_READ_LINE_ALONE_EXCEEDS_BYTE_LIMIT_VAR_0(this,TOOL_RESULT_READ_LINE_ALONE_EXCEEDS_BYTE_LIMIT_VAR_2,"f")} alone exceeds ${TOOL_RESULT_READ_LINE_ALONE_EXCEEDS_BYTE_LIMIT_VAR_0(this,TOOL_RESULT_READ_LINE_ALONE_EXCEEDS_BYTE_LIMIT_VAR_3,"f")}-byte limit. The read tool cannot return part of a line, so view_range cannot narrow this further.
