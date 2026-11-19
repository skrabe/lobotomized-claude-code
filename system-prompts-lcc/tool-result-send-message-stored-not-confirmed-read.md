<!--
name: 'Tool Result: SendMessage stored, not confirmed read'
description: >-
  SendMessage result clause that the message is stored for the session but not
  confirmed read, and a delivery notice may follow
ccVersion: 2.1.328
-->
; stored for that session, not confirmed read. If it reports within about 10 minutes that it held, refused or dropped the message, a [Cross-session delivery notice] follows. An older version may drop it and report nothing, so silence does not mean agreement
