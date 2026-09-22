<!--
name: 'Tool Result: Notify When Idle Blanked Not Pure Subscription'
description: >-
  SendMessage tool-result when a permission handler emptied the message: nothing
  was sent and the blanked call is not reinterpreted as a pure idle
  subscription.
ccVersion: 2.1.237
-->
A permission handler emptied this message; nothing was sent, and no idle subscription was made (a blanked delivery is never reinterpreted as a pure subscription — send notify_when_idle without a message if that is what you want).
