<!--
name: 'Tool Description: Self-hosted runner get pool'
description: >-
  Description/prompt of the self_hosted_runner_get_pool tool; injected as that
  tool's description when the self-hosted runner doctor toolset is enabled.
ccVersion: 2.1.224
-->
Read a self-hosted environment's aggregate state (alive_runner_count, available_capacity_total, capacity_in_use, pending_session_count, unplaceable_session_count, backing_off_count, circuit_broken_count).${"\nThe result includes an `equivalent.ui` string with the Admin-UI path. Surface it to the operator so they can repeat the action without you.\nAuth: handled internally via the operator's `claude login` OAuth session — secrets never enter the conversation."}
