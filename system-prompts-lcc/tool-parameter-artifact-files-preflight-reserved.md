<!--
name: 'Tool Parameter: Artifact Files Preflight Reserved'
description: >-
  files parameter description sentence reserving preflight.js at the artifact
  root as a small default-export ES module.
ccVersion: 2.1.267
-->
 `preflight.js` at the artifact root is reserved — it runs against open pages when you publish updates; it must be a ≤ 8 KiB ES module whose default export is a function, or the publish is refused.
