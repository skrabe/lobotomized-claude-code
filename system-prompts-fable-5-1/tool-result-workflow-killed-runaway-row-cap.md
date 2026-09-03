<!--
name: 'Tool Result: Workflow Killed Runaway Row Cap'
description: >-
  Workflow-run settlement error when the per-run row cap is exceeded (runaway
  rule), telling the model how to inspect retracted facts.
ccVersion: 2.1.259
-->
killed (runaway): the run exceeded the per-run row cap — usually a rule putting the fact it fires on. Its facts are readable with read {status:'retracted'}; fix the rule (or split a genuinely larger workload) before launching again.
