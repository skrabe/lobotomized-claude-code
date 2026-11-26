<!--
name: 'System reminder: project uploads not copied'
description: >-
  Tells Claude how many of the project's uploaded files were not copied to the
  project folder.
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_PROJECT_UPLOADS_NOT_COPIED_VAR_0
  - SYSTEM_REMINDER_PROJECT_UPLOADS_NOT_COPIED_VAR_1
-->
${SYSTEM_REMINDER_PROJECT_UPLOADS_NOT_COPIED_VAR_0.uploads} of the project's ${SYSTEM_REMINDER_PROJECT_UPLOADS_NOT_COPIED_VAR_0.ofUploads} uploaded ${SYSTEM_REMINDER_PROJECT_UPLOADS_NOT_COPIED_VAR_1(SYSTEM_REMINDER_PROJECT_UPLOADS_NOT_COPIED_VAR_0.ofUploads,"file")} ${SYSTEM_REMINDER_PROJECT_UPLOADS_NOT_COPIED_VAR_1(SYSTEM_REMINDER_PROJECT_UPLOADS_NOT_COPIED_VAR_0.uploads,"was","were")} not copied to ${this.deps.folder}.
