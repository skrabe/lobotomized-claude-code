<!--
name: 'Tool result: app action would-activate unsafe delivery'
description: >-
  Non-click action could not be delivered safely in the background (input watch,
  misbehaving control, screen reader); retry once.
ccVersion: 2.1.330
-->
this could not be delivered safely in the background right now, so it was NOT sent: the check that watches for stray real input could not be started, this control misbehaved under background input a little earlier, or a screen reader is running (it would read every focus change aloud). Retry once; if it repeats, this step cannot be done in the background
