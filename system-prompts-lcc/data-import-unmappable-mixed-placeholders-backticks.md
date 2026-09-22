<!--
name: 'Data: Import Unmappable Mixed Placeholders And Backticks'
description: >-
  `reason` for a foreign command that mixes argument placeholders with backticks
  or '!', interpolated into the /import summary prompt sent to the model.
ccVersion: 2.1.214
-->
Mixes argument placeholders with backticks or '!' outside its shell blocks — argument substitution at invocation time could assemble a live shell-exec marker from them. Port it manually.
