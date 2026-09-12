<!--
name: 'Tool Parameter: Artifact Files Preflight Reserved (Claude Voice)'
description: >-
  files schema sentence reserving preflight.js as a small default-export
  JavaScript module that runs when Claude publishes updates.
ccVersion: 2.1.269
-->
 `preflight.js` at the artifact root is reserved: it runs against open pages when Claude publishes updates, and it must be a JavaScript module of at most 8 KiB whose default export is a function, or the publish is refused.
