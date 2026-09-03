<!--
name: 'Workshop Verifier: Unknown Data Island'
description: >-
  Verifier violation hint returned when a workshop page contains a JSON script
  element other than the ws-decisions island.
ccVersion: 2.1.219
-->
Only the ws-decisions island may use a JSON script element — the session extracts the island mechanically, and a second JSON block could confuse that extraction.
