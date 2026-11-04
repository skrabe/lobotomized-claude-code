<!--
name: Resume Continue Prompt
description: >-
  Model-facing resume prompt (aqn() env-fallback returning
  CLAUDE_CODE_RESUME_PROMPT or this literal, isMeta) injected as a user message
  on interrupted-turn and deferred-tool auto-resume.
ccVersion: 2.1.291
-->

Continue from where you left off. This session restarted after its process exited unexpectedly; the user has not sent a new message since. Work in flight may have run without a recorded result. Inspect current files, branch state and running processes before retrying it.
