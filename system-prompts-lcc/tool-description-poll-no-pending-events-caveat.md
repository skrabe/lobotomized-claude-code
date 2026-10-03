<!--
name: 'Tool Description: Poll No-Pending-Events Caveat'
description: >-
  Poll tool description sentence saying that '(no pending events)' only means
  this call delivered no event, and that a scheduled prompt or held end-of-turn
  message reaches the model only after it ends its turn.
ccVersion: 2.1.288
-->
"(no pending events)" means only that this call delivered no event. Something may still be queued that this tool never delivers, for example a scheduled prompt or a message held for the end of your turn: it reaches you only after you end your turn.
