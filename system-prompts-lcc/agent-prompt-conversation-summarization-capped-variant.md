<!--
name: 'Agent Prompt: Conversation summarization (capped variant)'
description: >-
  Asks for a summary of the entire conversation in 2000 words or fewer inside
  summary tags, preserving facts, file paths, function names, error messages and
  open threads
ccVersion: 2.1.291
variables:
  - SECURITY_INSTRUCTIONS_PRESERVATION_NOTE
  - USER_MESSAGE_ATTRIBUTION_GUARD
-->
Summarize the entire conversation above in 2000 words or fewer, preserving all facts, file paths, function names, error messages, and open threads. Output only the summary, inside <summary></summary> tags.

${SECURITY_INSTRUCTIONS_PRESERVATION_NOTE}${USER_MESSAGE_ATTRIBUTION_GUARD}

There may be additional summarization instructions provided in the included context. If so, remember to follow these instructions when creating the summary.
