<!--
name: 'Agent Prompt: WebFetch summarizer quote-restricted instruction'
description: >-
  Instructs the summarizer model to answer only from the page above and appends
  the quote-length and reproduction restrictions
ccVersion: 2.1.232
variables:
  - AGENT_PROMPT_WEBFETCH_SUMMARIZER_QUOTE_RESTRICTED_INSTRUCTION_VAR_0
-->
Provide a concise response based only on the content above. In your response:
${AGENT_PROMPT_WEBFETCH_SUMMARIZER_QUOTE_RESTRICTED_INSTRUCTION_VAR_0}
