<!--
name: 'Tool Description: SendMessage @parent row'
description: >-
  Recipient table row for @parent (and optional @find row) in the SendMessage
  prompt.
ccVersion: 2.1.331
variables:
  - TOOL_DESCRIPTION_SENDMESSAGE_PARENT_RECIPIENT_ROW_VAR_0
-->

| \`"@parent"\` | The session that created this one |${TOOL_DESCRIPTION_SENDMESSAGE_PARENT_RECIPIENT_ROW_VAR_0?'\n| `"@find"` | Sends nothing: returns your user\'s sessions whose title is `options.session_name`, with their ids |':""}
