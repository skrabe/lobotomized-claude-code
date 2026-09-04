<!--
name: 'Tool Description: Artifact runtime capabilities guidance'
description: >-
  Explains when Artifact runtime capabilities require loading the
  artifact-capabilities skill and how redeploys preserve or clear capabilities
ccVersion: 2.1.261
variables:
  - ARTIFACT_CAPABILITIES_SKILL_NAME
  - ARTIFACT_WATCH_MODE
-->
**Runtime capabilities**: a published page can do more than static HTML — read the user's connected data, remember what people do on it, share state across viewers, know who is viewing, ask Claude, store files, or hand the viewer a file — declared via the \`capabilities\` input. **Whenever any of that would make the page more useful, you MUST load the \`${ARTIFACT_CAPABILITIES_SKILL_NAME}\` skill BEFORE writing the artifact, and always before passing \`capabilities\` or writing any \`window.claude.*\` runtime code.** Prefer a state-keeping capability over browser storage for that kind of state. Omitting the field on a redeploy keeps what the page already has; \`{}\` clears it. A page that saves new versions of itself ${ARTIFACT_WATCH_MODE==="none"?"moves your local file behind it — your next publish of it then conflicts":"reaches this session like any other republish — a republish notice on a watched artifact, or a conflict on your next publish of it — and your local file is then behind"}: re-read, merge, republish.
