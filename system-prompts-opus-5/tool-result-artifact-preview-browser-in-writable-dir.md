<!--
name: 'Artifact Preview: Browser Binary In Writable Directory'
description: >-
  Permission-deny and call() error when Chrome would launch from a directory
  this session can write without asking.
ccVersion: 2.1.247
-->
the browser preview would launch lives somewhere this session's commands can write without asking (a working directory, temp dir, or sandbox write root), where they could have planted or altered it — install Chrome outside those, or point BUN_CHROME_PATH at one from your shell.
