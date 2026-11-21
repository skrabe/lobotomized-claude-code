<!--
name: 'Tool result: display call busy'
description: >-
  Refusal because another screen/mouse/keyboard call of the session is in
  progress.
ccVersion: 2.1.330
-->
Not run: another screen, mouse or keyboard call of this session is still in progress, so nothing was sent. Calls that use the screen, mouse or keyboard run one at a time. Wait a few seconds (a wait action is not held back by this), then retry if still wanted. If it is still refused after several minutes and no approval dialog is waiting for the user, that call is probably stuck: tell the user that restarting Claude on the computer where it's running clears it; in the Claude desktop app, so does stopping this conversation and starting a new one.
