<!--
name: 'Skill: Steward pull request in other repository'
description: >-
  Refuses because the pull request belongs to a different repository than the
  checkout
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_PR_IN_OTHER_REPOSITORY_VAR_0
  - SKILL_STEWARD_PR_IN_OTHER_REPOSITORY_VAR_1
  - SKILL_STEWARD_PR_IN_OTHER_REPOSITORY_VAR_2
-->
That pull request is in ${SKILL_STEWARD_PR_IN_OTHER_REPOSITORY_VAR_0?.[1]}, but this checkout is of ${SKILL_STEWARD_PR_IN_OTHER_REPOSITORY_VAR_1.here}. Run ${SKILL_STEWARD_PR_IN_OTHER_REPOSITORY_VAR_2} from a checkout of ${SKILL_STEWARD_PR_IN_OTHER_REPOSITORY_VAR_0?.[1]}.
