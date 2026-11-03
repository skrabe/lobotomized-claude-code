<!--
name: 'Tool Result: Email file reference attachment unsafe filename'
description: >-
  Refuses an unsafe or over-long attachment filename and states the
  120-character single-line naming rules
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNSAFE_FILENAME_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNSAFE_FILENAME_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNSAFE_FILENAME_VAR_2
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNSAFE_FILENAME_VAR_3
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNSAFE_FILENAME_VAR_0}'s ${TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNSAFE_FILENAME_VAR_1(TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNSAFE_FILENAME_VAR_2)} holds a line break, a control character, an invisible or direction-changing character (such as a zero-width space or U+202E), a private-use character, U+FFFD, more than four combining marks on one character or more than four stacking signs (such as Khmer's coeng) in one stack of letters, a double quote ("), a backslash, a slash, a semicolon, "=?" or a percent escape such as %2F, has no letter or digit, or is longer than 120 characters, ${TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNSAFE_FILENAME_VAR_3} Make the call again with a name of at most 120 characters on one line, without those characters and with at least one letter or digit (for "=?", a space between "=" and "?" is enough).
