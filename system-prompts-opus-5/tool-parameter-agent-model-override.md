<!--
name: 'Tool Parameter: Agent Model Override'
description: >-
  Task/agent model param: optional per-agent model override; ignored for fork
  subagents which inherit the parent model.
ccVersion: 2.1.251
-->
Optional model override for this agent. Takes precedence over the agent definition's model frontmatter and the configured default subagent model. If omitted, uses the agent definition's model, else the default (inherits from the parent unless a default subagent model is configured). Ignored for subagent_type: "fork" — forks always inherit the parent model.
