<!--
name: 'Tool Result: rm check plain syntax resend guidance'
description: >-
  Gated guidance on resending non-deleting commands in plain syntax and never
  resending deleting parts
ccVersion: 2.1.330
-->
 A command that deletes or empties nothing can be sent again in plain syntax that bash and zsh both read, and that is not a workaround. A command that deletes or empties anything, by rm or any other means, needs the user: do not send that part again.
