<!--
name: Computer-use teach-mode permission block
description: >-
  Tool-result telling the model permissions cannot be requested during teach
  mode.
ccVersion: 2.1.206
-->
Cannot request additional permissions during teach mode — the permission dialog would be hidden. End teach mode (finish the tour or let the turn complete), then call request_access, then start a new tour.
