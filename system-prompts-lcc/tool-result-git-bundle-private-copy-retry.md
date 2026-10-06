<!--
name: 'Tool result: git bundle private copy retry'
description: >-
  Fallback remedy clause: retry, and if it recurs check git status to see
  whether git still reads this checkout.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_COPY_RETRY_VAR_0
-->
 Retry; if it keeps happening, first ${TOOL_RESULT_GIT_BUNDLE_PRIVATE_COPY_RETRY_VAR_0} \`git status\` here shows whether git itself still reads this checkout.
