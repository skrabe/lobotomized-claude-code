<!--
name: >-
  Tool result: SendMessage session service handoff failed (title without \u
  codes)
description: >-
  Refusal under pgr() telling Claude to resend with only allowed fields and a
  title written in its own characters, then tell the user if refused again.
ccVersion: 2.1.331
-->
Not sent: this call could not be handed to the session service. Send it once more, with no fields but `to`, `message`, `summary` and `options`, and write a title in its own characters, not as \u codes. If it is refused again, tell your user.
