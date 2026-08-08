<!--
name: Loop Noop Flag Guidance
description: >-
  Autonomous-loop prompt fragment (appended to F4t in Gda) instructing when to
  set noop true/false and noting consecutive noop ticks fold into one context
  entry.
ccVersion: 2.1.210
-->
Consecutive `noop: true` ticks are collapsed in the user's terminal view and tracked as a streak, so long quiet holds stay legible to the user without scrolling.
