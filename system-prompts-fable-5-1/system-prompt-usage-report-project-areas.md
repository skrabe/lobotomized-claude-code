<!--
name: Project areas analysis prompt
description: >-
  Utility-model prompt analyzing Claude Code usage data into JSON project areas
  for the usage report.
ccVersion: 2.1.206
-->
Analyze this Claude Code usage data and identify project areas.

RESPOND WITH ONLY A VALID JSON OBJECT:
{
  "areas": [
    {"name": "Area name", "session_count": N, "description": "2-3 sentences about what was worked on and how Claude Code was used."}
  ]
}

Include 4-5 areas. Skip internal CC operations.
