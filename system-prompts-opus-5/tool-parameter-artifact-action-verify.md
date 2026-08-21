<!--
name: 'Tool Parameter: Artifact Action Verify'
description: >-
  Addendum to the Artifact action parameter describing verify and that an empty
  diagnostic result is not a clean render.
ccVersion: 2.1.238
-->
 'verify' reads the runtime diagnostics (console output, uncaught errors, failed resource loads, capability-call outcomes) that viewers' browsers captured for an artifact's current version — pass `url`, or omit it to target this session's most recent publish. An empty result can mean no viewer has loaded the version yet, which is NOT evidence of a clean render.
