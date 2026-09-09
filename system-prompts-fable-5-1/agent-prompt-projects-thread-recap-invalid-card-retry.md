<!--
name: 'Agent Prompt: Projects Thread Recap Invalid Card Retry'
description: >-
  Retry user message for the projects-thread-recap agent_classifier side query
  when the previous response was not a valid card JSON object.
ccVersion: 2.1.265
variables:
  - AGENT_PROMPT_PROJECTS_THREAD_RECAP_INVALID_CARD_RETRY_VAR_0
-->
${AGENT_PROMPT_PROJECTS_THREAD_RECAP_INVALID_CARD_RETRY_VAR_0}

Previous response was not a valid card. Respond with ONLY the JSON object: state must be one of needs_reply, needs_approval, done, failed, working, and happened must not be empty.
