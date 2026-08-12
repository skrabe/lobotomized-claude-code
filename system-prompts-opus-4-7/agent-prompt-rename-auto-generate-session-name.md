<!--
name: 'Agent Prompt: /rename auto-generate session name'
description: >-
  Prompt used by /rename (no args) to auto-generate a kebab-case session name
  from conversation context
ccVersion: 2.1.148
-->
Generate a short kebab-case name (2-4 words) that captures the main topic of this conversation. Use lowercase words separated by hyphens. Return JSON with a "name" field.
