<!--
name: 'Data: Steward GitLab note body'
description: >-
  GitLab note body as given to the steward, with the internal-note marker in
  front when it applies
ccVersion: 2.1.331
variables:
  - DATA_STEWARD_GITLAB_NOTE_BODY_VAR_0
  - DATA_STEWARD_GITLAB_NOTE_BODY_VAR_1
-->
${DATA_STEWARD_GITLAB_NOTE_BODY_VAR_0.internal===!0?`[An internal note, which not everybody who sees the project may read: repeat nothing of it in a commit, a file or a branch.]
`:""}${DATA_STEWARD_GITLAB_NOTE_BODY_VAR_1((DATA_STEWARD_GITLAB_NOTE_BODY_VAR_0.body??"").replace(/\r\n?/g,`
`))}
