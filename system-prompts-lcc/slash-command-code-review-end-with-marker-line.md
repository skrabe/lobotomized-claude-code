<!--
name: 'Slash Command: Code Review End-With-Marker Line'
description: >-
  Trailing instruction appended to the inline /code-review prompt telling the
  model to end its response with an exact marker line; injected only when RCp()
  supplies a marker for a non-fork, non-ultra inline review.
ccVersion: 2.1.224
variables:
  - SLASH_COMMAND_CODE_REVIEW_END_WITH_MARKER_LINE_VAR_0
-->


After you finish the review, end your response with this exact line on its own:
${SLASH_COMMAND_CODE_REVIEW_END_WITH_MARKER_LINE_VAR_0}
