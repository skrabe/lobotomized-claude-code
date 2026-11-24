<!--
name: 'Skill: Steward gh finds no such pull request'
description: >-
  Says gh finds no pull request with the given number in this repository so
  nothing was done, and to check the number or run the command without one to
  take the branch's own; relayed verbatim through ne
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_GH_NO_SUCH_PULL_REQUEST_VAR_0
  - SKILL_STEWARD_GH_NO_SUCH_PULL_REQUEST_VAR_1
-->
gh finds no pull request #${SKILL_STEWARD_GH_NO_SUCH_PULL_REQUEST_VAR_0[2]} in this repository, so I did nothing. Check the number, or run ${SKILL_STEWARD_GH_NO_SUCH_PULL_REQUEST_VAR_1} without one to take this branch's own.
