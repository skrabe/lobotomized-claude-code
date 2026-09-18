<!--
name: 'Data: sandbox.credentials.files.extract setting description (part 1 of 3)'
description: >-
  Description of the `sandbox.credentials.files.extract` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Optional regex for structured masking when mode is `mask`. Applied globally to the file; capture group 1 of each match is a credential value, and only those captured spans are replaced 
