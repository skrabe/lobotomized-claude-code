<!--
name: 'Agent Prompt: Artifact Comment Follow-Up Another Comment'
description: >-
  Follow-up message injected into a running artifact-comment background agent
  when another comment arrives on the same thread.
ccVersion: 2.1.269
variables:
  - AGENT_PROMPT_ARTIFACT_COMMENT_FOLLOW_UP_ANOTHER_COMMENT_VAR_0
  - AGENT_PROMPT_ARTIFACT_COMMENT_FOLLOW_UP_ANOTHER_COMMENT_VAR_1
-->
Another comment sent to Claude has arrived on thread ${AGENT_PROMPT_ARTIFACT_COMMENT_FOLLOW_UP_ANOTHER_COMMENT_VAR_0.threadId} of artifact ${AGENT_PROMPT_ARTIFACT_COMMENT_FOLLOW_UP_ANOTHER_COMMENT_VAR_0.url} while you are working on it. Re-read the thread (${AGENT_PROMPT_ARTIFACT_COMMENT_FOLLOW_UP_ANOTHER_COMMENT_VAR_1()}) and cover it too — in the same reply if you have not replied yet, otherwise in one further reply.
