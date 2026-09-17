<!--
name: 'Data: Task notification artifact watches dropped after sign-out'
description: >-
  Task-notification event body saying watches opened by the signed-out account
  no longer report republishes or comments, and not to re-watch unasked
ccVersion: 2.1.274
-->
Those watches were opened as the account that signed out: this session no longer keeps track of new versions of those artifacts or hears comments on them, and their comment auto-replies are off. A publish or watch of yours once someone is signed in opens a fresh watch; do not re-watch just to resume listening unless the user asks.
