<!--
name: 'Git bundle: retry remedy'
description: Generic retry remedy suffix pointing at the index link check and git status
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_COPY_RETRY_VAR_0
-->
 Retry; if it keeps happening, first ${TOOL_RESULT_GIT_BUNDLE_PRIVATE_COPY_RETRY_VAR_0}; \`git status\` here then shows whether git itself still reads this checkout.
