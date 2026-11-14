<!--
name: 'Tool result: Artifacts refused personal login in restricted sandbox'
description: >-
  Artifacts refusal when a personal login or token is used inside an
  Anthropic-hosted restricted-network sandbox; tells Claude to inform the user
  and not retry.
ccVersion: 2.1.325
-->
Artifacts refused this sign-in because Claude Code is using a person's own login or token inside an Anthropic-hosted sandbox with restricted network access. That doesn't show whether any artifact exists or who can open it. The user can remove the login or token they added and let the cloud session make the call under its own sign-in, or run Claude Code outside the sandbox. Tell the user, and don't retry or try another way from this session
