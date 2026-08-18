<!--
name: 'Tool result: Artifact resume replies interrupted'
description: >-
  Reports that the resume request was interrupted before the live watch
  connected, leaving the stop in place
ccVersion: 2.1.234
-->
Auto-replies were NOT resumed: the request was interrupted before the live watch finished connecting, so the auto-reply stop stays in place (a connection already under way may still complete as a plain version watch — action "status" shows it). Ask the user, and call resume_replies again only if they still want auto-replies resumed.
