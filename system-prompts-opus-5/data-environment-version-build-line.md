<!--
name: 'Data: Version and build line'
description: >-
  Environment line naming the running Claude Code version and build metadata,
  injected into the model context.
ccVersion: 2.1.224
variables:
  - DATA_ENVIRONMENT_VERSION_BUILD_LINE_VAR_0
-->
${DATA_ENVIRONMENT_VERSION_BUILD_LINE_VAR_0} (built ${{ISSUES_EXPLAINER:"report the issue at https://github.com/anthropics/claude-code/issues",PACKAGE_URL:"@anthropic-ai/claude-code",README_URL:"https://code.claude.com/docs/en/overview",VERSION:"<<CCVERSION>>",FEEDBACK_CHANNEL:"https://github.com/anthropics/claude-code/issues",BUILD_TIME:"<<BUILD_TIME>>",GIT_SHA:"8a2a469b68f918917492973f3b16bd1682b9f82c",DD_SOURCEMAP_GROUP:"darwin"}.BUILD_TIME})
