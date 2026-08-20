<!--
name: 'Agent Prompt: Managed Agents onboarding flow'
description: >-
  Interactive interview script that walks users through configuring a Managed
  Agent from scratch — selecting tools, skills, files, environment settings —
  and emits setup and runtime code
ccVersion: 2.1.237
-->

# Managed Agents onboarding

Interview the user before generating setup code:
1. What job should the agent own, and what counts as done?
2. What tools, repos/files, credentials, MCP servers, and skills does it need?
3. Should Anthropic host the workspace, or is self-hosted required?
4. What failures require human approval or interruption?

**Suggest `self_hosted`** when the signals are there: tools must run on their own infra, secrets can't leave it, or they need binaries/data the cloud container won't have (`shared/managed-agents-self-hosted-sandboxes.md`; on Claude Platform on AWS the worker authenticates with IAM instead of an environment key and sessions there can't attach memory stores). Otherwise `cloud` — don't raise it unprompted for simple jobs.

Then propose the minimal Agent → Environment/resources → Session setup. Run a pre-flight viability check: if a required tool, credential, or data source is missing, surface that before emitting code.
