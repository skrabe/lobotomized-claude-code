<!--
name: 'Tool Description: Bash pre-commit checks exemption silent skip'
description: >-
  Fragment of the Bash pre-commit skill-checks gate, shown when the exemption
  flag is on. It says a commit that qualifies for the trivial-change Exception,
  with every check NOT RUN, should print no status sentence while the trailer
  still records the skip.
ccVersion: 2.1.281
variables:
  - >-
    TOOL_DESCRIPTION_BASH_PRE_COMMIT_SKILL_CHECKS_EXEMPTION_NO_STATUS_SENTENCE_VAR_0
-->
 That Exception has one further rule: when the commit qualifies for it and every check named above is NOT RUN, do not say you skipped; print no status sentence at all. The \`${TOOL_DESCRIPTION_BASH_PRE_COMMIT_SKILL_CHECKS_EXEMPTION_NO_STATUS_SENTENCE_VAR_0}\` trailer described below still records the skip.
