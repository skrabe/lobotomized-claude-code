<!--
name: Not a protocol frame
description: >-
  SendMessage validation error returned to the model to send plain text, not a
  protocol frame.
ccVersion: 2.1.206
-->
message text must not be a teammate protocol frame (permission/mode/plan/shutdown JSON) — to respond to a plan or shutdown request, use the structured object form ({"message": {"type": ...}}); otherwise send plain text
