<!--
name: 'System Reminder: turn not ended, sibling call failed (no repeat)'
description: >-
  Meta note that an end-turn request was ignored because another call in the
  same message failed; successful calls should not be repeated.
ccVersion: 2.1.331
-->
The turn did not end: a tool call in your last message asked to end it, but another call in that message failed. The calls that succeeded took effect, so do not repeat them.
