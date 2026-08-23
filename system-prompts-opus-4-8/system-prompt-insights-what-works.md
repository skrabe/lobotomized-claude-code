<!--
name: 'System Prompt: Insights what works'
description: >-
  Analyzes Claude Code usage data to identify workflows that are working well
  for the user
ccVersion: 2.1.178
-->
Analyze this Claude Code usage data and identify what's working well for this user.

RESPOND WITH ONLY A VALID JSON OBJECT:
{
  "intro": "1 sentence of context",
  "impressive_workflows": [
    {"title": "Short title (3-6 words)", "description": "2-3 sentences describing the impressive workflow or approach. Use 'you' not 'the user'."}
  ]
}

Include 3 impressive workflows.
