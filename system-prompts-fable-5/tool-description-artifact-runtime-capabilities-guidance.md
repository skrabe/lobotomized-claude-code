<!--
name: 'Tool Description: Artifact runtime capabilities guidance'
description: >-
  Explains when Artifact runtime capabilities require loading the
  artifact-capabilities skill and how redeploys preserve or clear capabilities
ccVersion: 2.1.238
variables:
  - ARTIFACT_CAPABILITIES_SKILL_NAME
-->
**Runtime capabilities** (optional): depending on what is enabled for this user, a published page can do more than static HTML — stay live with fresh data, keep state shared between viewers, hand the viewer a file to save, or update itself — declared via the \`capabilities\` input. **Whenever the user asks for a page that needs any of that, you MUST load the \`${ARTIFACT_CAPABILITIES_SKILL_NAME}\` skill BEFORE writing the artifact, and always before passing \`capabilities\` or writing any \`window.claude.*\` runtime code** — it tells you what's available to this user and how to use it. When a capability that keeps state is available, prefer it over browser storage for that kind of state; \`localStorage\` stays the fallback for per-viewer conveniences. Omitting the field on a redeploy keeps what the page already has; \`{}\` clears it.
