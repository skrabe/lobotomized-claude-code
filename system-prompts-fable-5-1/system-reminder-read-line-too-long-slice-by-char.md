<!--
name: 'System Reminder: Read line too long, slice by char'
description: >-
  guidance injected when a file's lines exceed Read's offset/limit, suggesting
  Bash character-range slicing
ccVersion: 2.1.178
variables:
  - SYSTEM_REMINDER_READ_LINE_TOO_LONG_SLICE_BY_CHAR_VAR_0
  - SYSTEM_REMINDER_READ_LINE_TOO_LONG_SLICE_BY_CHAR_VAR_1
-->

When Read cannot handle a file's long lines, slice it by character range with Bash: ${SYSTEM_REMINDER_READ_LINE_TOO_LONG_SLICE_BY_CHAR_VAR_0} -c 'print(open("${SYSTEM_REMINDER_READ_LINE_TOO_LONG_SLICE_BY_CHAR_VAR_1}").read()[A:B])' in ~${SYSTEM_REMINDER_READ_LINE_TOO_LONG_SLICE_BY_CHAR_VAR_2}-character spans until the file has been read completely.
