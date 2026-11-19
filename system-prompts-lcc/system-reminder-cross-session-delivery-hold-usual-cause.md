<!--
name: 'System Reminder: Cross-session delivery hold usual cause'
description: >-
  Explains that holds usually come from differing permission modes or a
  hold-every-message setting, and how terminal, cloud and desktop sessions
  handle approval
ccVersion: 2.1.328
-->
The usual cause is that the two sessions are in different permission modes; a session can also be set to hold every message. A terminal session asks its user for approval. A cloud session or the desktop app may show nothing to approve: then it takes a change to that session's permission mode or its crossSessionInbound setting, which is for its user to decide.
