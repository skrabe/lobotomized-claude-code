<!--
name: 'Skill: claude-code-guide — `claude plugin eval` trust warning'
description: >-
  Third fragment of the `claude plugin eval` line in the claude-code-guide
  skill's Current Build subcommand list: trust, sandbox limits, and
  --trust-plugin for CI.
ccVersion: 2.1.269
-->
It loads the plugin and runs its eval suite (prompts, graders; scaffold scripts and real MCP servers only when you opt in) on your machine, as you: only evaluate plugins you trust — the run's sandboxing limits what a malicious plugin can reach but is not a guarantee, and a bundled suite passing is not a security vetting. The first run in an untrusted plugin directory asks you to confirm (--trust-plugin answers for CI)
