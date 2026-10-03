<!--
name: 'Tool Result: Read Long-Lines Char-Range Guidance'
description: >-
  Read guidance noting a file's lines are too long for offset/limit chunking;
  slice by character range instead.
ccVersion: 2.1.288
variables:
  - TOOL_DESCRIPTION_READ_LONG_LINES_CHAR_RANGE_GUIDANCE_VAR_0
-->
- Note: this file's lines are too long for ${TOOL_DESCRIPTION_READ_LONG_LINES_CHAR_RANGE_GUIDANCE_VAR_0}'s offset/limit chunking. Slice by character range instead (e.g. python read()[A:B], dd, or cut -c).
