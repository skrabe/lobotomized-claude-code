<!--
name: Artifact Durable Wake Session Device Bound
description: >-
  Durable-wake failure reason: a desktop-bound cloud session cannot register an
  artifact wake subscription.
ccVersion: 2.1.268
-->
This cloud session is bound to the desktop it was started from (Cowork or `claude --cloud`), and that device's trusted-device check means activity on the artifact can't wake it, so no wake subscription was registered. Publishing and reading still work; retrying won't help in this session.
