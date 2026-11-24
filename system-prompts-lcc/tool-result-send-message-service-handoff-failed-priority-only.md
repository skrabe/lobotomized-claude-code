<!--
name: 'Tool result: SendMessage session service handoff failed (priority only)'
description: >-
  Refusal telling Claude to resend with only to, message, summary and
  options.priority, then tell the user if refused again.
ccVersion: 2.1.331
-->
Not sent: this call could not be handed to the session service. Send it once more, with no fields but `to`, `message`, `summary` and `options.priority`. If it is refused again, tell your user.
