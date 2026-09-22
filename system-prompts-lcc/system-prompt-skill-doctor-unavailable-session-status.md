<!--
name: 'System Prompt: Skill Doctor Unavailable Session Status'
description: >-
  Tells the model /skill-doctor is not in this session and not to instruct the
  user to run it here.
ccVersion: 2.1.261
-->
`/skill-doctor` is NOT available in this session. It is on by default in current releases; a session lacks it on an older release, or when this client does not receive feature settings (Bedrock/Vertex/Foundry, telemetry or non-essential traffic disabled, or a first launch that has not fetched them yet) and no administrator has switched it on. Describe it if asked and suggest updating or asking their administrator, but do not tell the user to run it here.
