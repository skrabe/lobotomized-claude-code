<!--
name: 'System Reminder: Attached machine outcome correction wake'
description: >-
  Resumes authorized work after the outcome of a previously abandoned remote
  command becomes known.
ccVersion: 2.1.295
-->
This session now knows what became of a command it had stopped waiting for on an attached computer; the correction note says what. Nobody typed this; it is not a request from the user. If work in this conversation was waiting on that command, continue it within what the user already asked for; anything that needed their go-ahead still does. If nothing is waiting on it, say so in one short line and stop.
