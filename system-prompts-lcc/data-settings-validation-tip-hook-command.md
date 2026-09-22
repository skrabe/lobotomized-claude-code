<!--
name: 'Data: settings validation tip (command hook without command)'
description: >-
  Suggestion appended to a settings.json validation error (command hook without
  command); the model reads it in the tool result when its edit to a settings
  file fails validation.
ccVersion: 2.1.276
-->
Command hooks require `command`. For exec form (no shell), set `command` to the executable and `args` to its arguments: {"type": "command", "command": "echo", "args": ["hi"]}. For shell form, set `command` to the full shell string: {"type": "command", "command": "echo hi"}.
