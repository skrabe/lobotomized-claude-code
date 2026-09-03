<!--
name: 'Skill: Code Review Posting To GitLab'
description: >-
  Code-review skill block telling the model how to post findings to a GitLab MR
  when --comment is set.
ccVersion: 2.1.257
variables:
  - SKILL_CODE_REVIEW_POSTING_TO_GITLAB_VAR_0
  - SKILL_CODE_REVIEW_POSTING_TO_GITLAB_VAR_1
  - SKILL_CODE_REVIEW_POSTING_TO_GITLAB_VAR_2
-->


## Posting to GitLab (--comment)

The \`--comment\` flag was passed. After producing the findings list, if the
review target is a GitLab merge request, post the findings as one general MR
note via \`${`glab mr note${SKILL_CODE_REVIEW_POSTING_TO_GITLAB_VAR_0?` ${SKILL_CODE_REVIEW_POSTING_TO_GITLAB_VAR_0}`:""}${SKILL_CODE_REVIEW_POSTING_TO_GITLAB_VAR_1} -m "<body>"`}\`${SKILL_CODE_REVIEW_POSTING_TO_GITLAB_VAR_2?"":" from inside that project's checkout"}
(every finding with its file:line, the issue, and the suggested fix). glab has no single verb for line-anchored
comments; those require \`glab api projects/:id/merge_requests/:iid/discussions\`,
so post the general note unless the user asks for inline threads. If glab is
not available in this session, print the findings instead. If the target is
not an MR, print the findings to the terminal and note that \`--comment\` was
ignored.
