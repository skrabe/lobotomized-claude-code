<!--
name: 'Slash command: PR Steward terms intro'
description: >-
  Opens the watch terms by saying Claude works on feedback and failing checks
  toward a mergeable change
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_PR_STEWARD_TERMS_INTRO_VAR_0
-->
Claude ${SLASH_COMMAND_PR_STEWARD_TERMS_INTRO_VAR_0?"reviews your change and works on feedback and failing checks to help get it":"works on feedback and failing checks to help get your change"} ready to merge. What can merge depends on your permissions and your repository's branch rules.
