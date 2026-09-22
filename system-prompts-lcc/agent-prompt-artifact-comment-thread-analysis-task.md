<!--
name: 'Agent Prompt: Artifact Comment Thread Analysis Task'
description: >-
  Dispatches an artifact-comment analyst agent to analyze a specific thread and
  return its analysis brief.
ccVersion: 2.1.227
variables:
  - AGENT_PROMPT_ARTIFACT_COMMENT_THREAD_ANALYSIS_TASK_VAR_0
  - AGENT_PROMPT_ARTIFACT_COMMENT_THREAD_ANALYSIS_TASK_VAR_1
  - AGENT_PROMPT_ARTIFACT_COMMENT_THREAD_ANALYSIS_TASK_VAR_2
-->
Analyze artifact comment thread ${AGENT_PROMPT_ARTIFACT_COMMENT_THREAD_ANALYSIS_TASK_VAR_0.id} on artifact ${AGENT_PROMPT_ARTIFACT_COMMENT_THREAD_ANALYSIS_TASK_VAR_1} (triggering comment id ${AGENT_PROMPT_ARTIFACT_COMMENT_THREAD_ANALYSIS_TASK_VAR_2.triggerComment.id}).
