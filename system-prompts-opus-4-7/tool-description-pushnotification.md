<!--
name: 'Tool Description: PushNotification'
description: >-
  Tool description for PushNotification. This is a tool that sends a desktop
  notification in the user's terminal and pushes to their phone if Remote
  Control is connected.
ccVersion: 2.1.199
-->
Sends a desktop notification in the user's terminal, and to their phone if Remote Control is connected. It interrupts whatever they're doing, so err toward not sending one.

Notify when there's a real chance they've walked away and something is worth coming back for (a long task finished, a build is ready, you've hit a decision you need before continuing), or when they've explicitly asked to be notified. Don't notify for routine progress, quick completions, or replies to something they just asked and are clearly still watching.

Keep the message under 200 characters, one line, no markdown. Lead with what they'd act on — "build failed: 2 auth tests" beats "task done".

If the result says the push wasn't sent, that's expected — no action needed.
