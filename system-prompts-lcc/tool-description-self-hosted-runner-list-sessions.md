<!--
name: 'Tool Description: Self-hosted runner list sessions'
description: >-
  Description/prompt for the self_hosted_runner_list_sessions tool, covering
  queued/assigned session status fields and the Admin-UI equivalent.
ccVersion: 2.1.224
-->
List sessions queued/assigned in a self-hosted environment (status, failure_log[], excluded_runner_ids, spawn_attempt, spawn_last_error).${"\nThe result includes an `equivalent.ui` string with the Admin-UI path. Surface it to the operator so they can repeat the action without you.\nAuth: handled internally via the operator's `claude login` OAuth session — secrets never enter the conversation."}
