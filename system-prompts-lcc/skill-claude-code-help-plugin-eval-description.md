<!--
name: 'Skill: claude-code-guide — `claude plugin eval [target]` description'
description: >-
  First fragment of the `claude plugin eval` line in the claude-code-guide
  skill's Current Build subcommand list: what the command runs and where it
  looks for cases.
ccVersion: 2.1.235
-->
Run eval cases (<eval dir>/**/case.yaml or prompt.md + graders/*.md; the eval dir is evals/ unless --eval-dir or the manifest says otherwise) against a plugin and report scored results. 
