<!--
name: 'Slash Command: Steward comment too long to read'
description: >-
  Reason the watch can't proceed: a comment exceeds the read limit so a stop
  request could be missed
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_COMMENT_TOO_LONG_UNREAD_VAR_0
  - SLASH_COMMAND_STEWARD_COMMENT_TOO_LONG_UNREAD_VAR_1
-->
a comment ${SLASH_COMMAND_STEWARD_COMMENT_TOO_LONG_UNREAD_VAR_0?`of ${SLASH_COMMAND_STEWARD_COMMENT_TOO_LONG_UNREAD_VAR_1.author.by}'s`:"by somebody whose words count"} is longer than I read (4,000 characters), so I could miss a request to stop. That holds until it is shorter${SLASH_COMMAND_STEWARD_COMMENT_TOO_LONG_UNREAD_VAR_0?", or a maintainer has hidden it":""}
