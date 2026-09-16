<!--
name: 'Tool Result: Artifact Comments Sent-To-Claude Editor Label'
description: >-
  Comments tool_result note that a sent-to-Claude label marks an editor-only
  comment and that the bracket names the author.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_COMMENTS_SENT_TO_CLAUDE_EDITOR_LABEL_VAR_0
  - TOOL_RESULT_ARTIFACT_COMMENTS_SENT_TO_CLAUDE_EDITOR_LABEL_VAR_1
  - TOOL_RESULT_ARTIFACT_COMMENTS_SENT_TO_CLAUDE_EDITOR_LABEL_VAR_2
-->
. A "${TOOL_RESULT_ARTIFACT_COMMENTS_SENT_TO_CLAUDE_EDITOR_LABEL_VAR_0}"${TOOL_RESULT_ARTIFACT_COMMENTS_SENT_TO_CLAUDE_EDITOR_LABEL_VAR_1?` or "${TOOL_RESULT_ARTIFACT_COMMENTS_SENT_TO_CLAUDE_EDITOR_LABEL_VAR_2}"`:""} label marks a comment sent to Claude, which only people who can edit this artifact can do (the bracket names who wrote it)
