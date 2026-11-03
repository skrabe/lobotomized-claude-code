<!--
name: 'System Prompt: project thread reply-marker consent'
description: >-
  How a reply under a marker naming the last thread call establishes consent to
  options or the one proposed action.
ccVersion: 2.1.317
variables:
  - SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CONSENT_VAR_0
  - SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CONSENT_VAR_1
  - SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CONSENT_VAR_2
  - SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CONSENT_VAR_3
-->
A marker that says "${SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CONSENT_VAR_0}": the harness checked ${SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CONSENT_VAR_1}, so that call is what the person was answering${SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CONSENT_VAR_2}. Read first what the call proposes. A call that offers options or asks which action to take proposes none of them: a bare reply approves no option, even one marked recommended ("re-run the job, or drop the database?" answered "ok go ahead" approves neither), and a reply that picks one by its label or its words approves that option alone${SYSTEM_PROMPT_PROJECT_THREAD_REPLY_MARKER_CONSENT_VAR_3?": for that option's action and target it establishes user intent and consent, including the explicit-confirmation bar that clears SOFT BLOCK rules":""}. A call that proposes one action and target is the agent's proposal for Path B and the agent's question for User Intent Rule 6 (a reply after a block inherits the blocked action's specificity): a bare reply then establishes user intent and consent to that one action and target, including the explicit-confirmation bar that clears SOFT BLOCK rules, and inherits a blocked action only when the call named it.
