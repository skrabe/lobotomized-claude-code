<!--
name: 'Agent Prompt: Code review wrap-in-analysis-tags'
description: 'Code review subagent: wrap analysis in <analysis> tags before final summary'
ccVersion: 2.1.291
variables:
  - AGENT_PROMPT_CODE_REVIEW_ANALYSIS_TAGS_VAR_0
-->
Before your final summary, wrap your analysis in <analysis> tags. In it, walk the recent messages in order and identify:

- The user's explicit requests and intents
- Your approach to addressing each
- Key decisions, technical concepts, and code patterns
- Specifics: file names, code snippets, function signatures, file edits
- Errors you hit and how you fixed them
- User feedback, especially anywhere the user asked you to do something differently
- ${AGENT_PROMPT_CODE_REVIEW_ANALYSIS_TAGS_VAR_0}

Then cross-check the analysis for technical accuracy before writing the summary.
