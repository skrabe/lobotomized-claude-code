<!--
name: 'Tool result: Artifact resume replies already connecting'
description: >-
  Reports that a resume could not attach because a reconnect for the artifact is
  already mid-boot
ccVersion: 2.1.234
-->
Auto-replies were NOT resumed: a connection for this artifact is already mid-boot (a reconnect in progress), and a resume cannot attach to it. The stop stays in place unless that connection is a fresh publish re-arming it — check action "status" first, and call resume_replies again only if it still reports stopped and the user still wants auto-replies resumed.
