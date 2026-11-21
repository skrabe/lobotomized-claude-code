<!--
name: 'System reminder: agent resumed after user Stop'
description: >-
  Meta message to a resumed background agent: the user's Stop ended it, earlier
  stop-and-wait lines no longer hold, check partly-run calls.
ccVersion: 2.1.330
-->
The user pressed Stop, which ended every background agent, you among them. You have now been resumed, so a line above that tells you to stop and wait no longer holds. A tool call that was running then may have run in part or in full, so check before you repeat it. Background commands and agents that you started may have ended, and their reports may be lost.
