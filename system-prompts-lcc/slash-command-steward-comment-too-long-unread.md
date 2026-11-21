<!--
name: 'Slash Command: Steward comment too long to read'
description: >-
  Reason the watch can't proceed: a comment exceeds the read limit so a stop
  request could be missed
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_STEWARD_COMMENT_TOO_LONG_UNREAD_VAR_0
-->
a comment of ${SLASH_COMMAND_STEWARD_COMMENT_TOO_LONG_UNREAD_VAR_0.author.by}'s is longer than I read (4,000 characters), so I could miss a request to stop. That holds until it is shorter, or a maintainer has hidden it
