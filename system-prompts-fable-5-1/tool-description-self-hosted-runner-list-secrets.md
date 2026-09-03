<!--
name: 'Tool Description: Self-hosted runner list secrets'
description: >-
  Description/prompt for the self_hosted_runner_list_secrets tool, covering
  metadata-only secret listing and the Admin-UI equivalent path.
ccVersion: 2.1.224
-->
List environment secrets (jti, label, created_at, revoked, last_used_at). Secret values are never returned — only metadata.${"\nThe result includes an `equivalent.ui` string with the Admin-UI path. Surface it to the operator so they can repeat the action without you.\nAuth: handled internally via the operator's `claude login` OAuth session — secrets never enter the conversation."}
