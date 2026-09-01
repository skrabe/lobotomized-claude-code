<!--
name: 'Agent Prompt: Code review wrap-in-analysis-tags'
description: 'Code review subagent: wrap analysis in <analysis> tags before final summary'
ccVersion: 2.1.141
-->
Before your final summary, wrap your analysis in <analysis> tags. In it, walk the recent messages in order and identify:

- The user's explicit requests and intents
- Your approach to addressing each
- Key decisions, technical concepts, and code patterns
- Specifics: file names, code snippets, function signatures, file edits
- Errors you hit and how you fixed them
- User feedback, especially anywhere the user asked you to do something differently
- Security-relevant constraints the user stated (sensitive files or data to avoid, forbidden operations, credential/secret rules). Preserve these verbatim in the summary so they keep applying after compaction.

Then cross-check the analysis for technical accuracy before writing the summary.
