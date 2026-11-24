<!--
name: 'Tool Result: Steward push check needs newer gh'
description: Steward hook refusal of a push when gh is too old to check what it carries
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_STEWARD_PUSH_GH_TOO_OLD_VAR_0
-->
this gh is too old to check what a push would carry: that takes gh ${TOOL_RESULT_STEWARD_PUSH_GH_TOO_OLD_VAR_0} or later. Trying again won't help. Push nothing, and tell the user to upgrade gh (gh --version shows which one they have) and then to start the watch again, since a new gh ends this one
