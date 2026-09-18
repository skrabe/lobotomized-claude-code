<!--
name: 'Data: hooks.hooks.(command).asyncRewake setting description'
description: >-
  Description of the `hooks.hooks.(command).asyncRewake` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
If true, hook runs in background and wakes the model on exit code 2 (blocking error). Implies async.
