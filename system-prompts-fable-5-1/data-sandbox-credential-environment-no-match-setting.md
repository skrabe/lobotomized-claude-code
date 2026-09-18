<!--
name: 'Data: Sandbox credential environment no-match setting'
description: >-
  Describes sandbox credential environment-variable onExtractNoMatch behavior,
  including warn, deny, error, and decode-path constraints
ccVersion: 2.1.276
-->
What to do when `extract` matches nothing in the value. `warn` (default) emits a stderr warning and lets the variable pass through unmasked (fail-open, for credentials that may be legitimately absent); `deny` unsets the variable inside the sandbox (fail-closed); `error` aborts at sandbox setup so nothing runs until the config is fixed. Only meaningful when mode is `mask` and `extract` is set without `decode`. On a mask entry with `decode`, the runtime takes the decode path and never consults this field, so a fail-closed setting 
