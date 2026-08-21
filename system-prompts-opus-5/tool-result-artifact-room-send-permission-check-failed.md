<!--
name: 'Tool Result: Artifact Room Send Permission Check Failed'
description: >-
  Fail-closed Artifact deny message when room_send cannot complete its
  permission check.
ccVersion: 2.1.238
-->
The permission check for this room_send failed before its approval could be shown, so nothing was sent. Retry after the underlying failure clears.
