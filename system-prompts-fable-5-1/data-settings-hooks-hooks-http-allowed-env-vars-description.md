<!--
name: 'Data: hooks.hooks.(http).allowedEnvVars setting description'
description: >-
  Description of the `hooks.hooks.(http).allowedEnvVars` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Explicit list of environment variable names that may be interpolated in header values. Only variables listed here will be resolved; all other $VAR references are left as empty strings. Required for env var interpolation to work.
