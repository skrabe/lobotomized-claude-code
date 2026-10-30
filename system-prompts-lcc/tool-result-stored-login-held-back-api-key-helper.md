<!--
name: 'Tool Result: Stored login held back by API key helper'
description: >-
  Error message (StoredLoginHeldBackError) explaining Claude Code did not send
  the claude.ai login because the administrator's API key helper is not in
  effect, returned when uploads or API calls are refused.
ccVersion: 2.1.314
-->
Claude Code didn't send your claude.ai login, because the API key helper your administrator set isn't in effect. Your organization's managed settings may be overriding it. Ask your administrator to keep the key helper and its API address in effect, to name Anthropic's API address in those managed settings, or to remove the key helper. Run /status to see your setting sources.
