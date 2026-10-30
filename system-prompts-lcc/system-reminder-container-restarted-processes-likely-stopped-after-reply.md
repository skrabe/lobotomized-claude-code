<!--
name: 'System Reminder: Container restarted processes likely stopped after reply'
description: >-
  Note in the container-restarted reminder that re-created processes are likely
  stopped after each reply, so run what must finish in the foreground or tell
  the user.
ccVersion: 2.1.314
-->
In this session every process left running is likely stopped a few minutes after each reply, so a command you re-create now will likely be stopped after your next reply too: run in the foreground, with a long enough `timeout`, any that must finish and can finish within the foreground maximum, and otherwise tell the user it will likely be stopped a few minutes after your reply.
