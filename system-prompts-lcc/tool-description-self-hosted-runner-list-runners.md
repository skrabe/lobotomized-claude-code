<!--
name: 'Tool Description: Self-hosted runner list runners'
description: >-
  Description/prompt for the self_hosted_runner_list_runners tool, listing
  per-runner lease and assignment fields plus the Admin-UI equivalent.
ccVersion: 2.1.224
-->
List runners registered to a self-hosted environment, with per-runner lease_expires_at, locked_account_id/email, and assigned_session_count.${"\nThe result includes an `equivalent.ui` string with the Admin-UI path. Surface it to the operator so they can repeat the action without you.\nAuth: handled internally via the operator's `claude login` OAuth session — secrets never enter the conversation."}
