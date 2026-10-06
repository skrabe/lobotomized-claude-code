<!--
name: Resume Continue Prompt
description: >-
  Model-facing resume prompt (aqn() env-fallback returning
  CLAUDE_CODE_RESUME_PROMPT or this literal, isMeta) injected as a user message
  on interrupted-turn and deferred-tool auto-resume.
ccVersion: 2.1.291
-->
Your response was cut off because it exceeded the output token limit. Continue from where you left off. What you write next is shown as a separate block below the text so far, so begin at the start of the line, table row, list item or sentence that was cut, writing it again in full, and if you were inside a code block or a table, open it again first (the same code fence and language, the table's header row). Repeat nothing before that point and do not comment on the interruption. Keep going until the response is complete.
