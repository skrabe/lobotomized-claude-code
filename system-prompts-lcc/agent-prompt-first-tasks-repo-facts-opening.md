<!--
name: 'Agent Prompt: First tasks repo facts opening'
description: >-
  Opening of the user message sent to the first-tasks suggester model: date,
  fence BEGIN, branch, default branch and change counts.
ccVersion: 2.1.330
variables:
  - AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_0
  - AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_1
  - AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_2
  - AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_3
-->
Today is ${AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_0.toLocaleDateString("en-US",{weekday:"long"})} ${AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_0.toLocaleDateString("en-CA")}.
BEGIN ${AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_1}
Current branch: ${AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_2(AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_3.branch)||"unknown"}. Default branch: ${AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_2(AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_3.defaultBranch)||"unknown"}. Uncommitted files: ${AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_3.uncommittedCount}. Files changed in the last 7 days: ${AGENT_PROMPT_FIRST_TASKS_REPO_FACTS_OPENING_VAR_3.changedCount}.
