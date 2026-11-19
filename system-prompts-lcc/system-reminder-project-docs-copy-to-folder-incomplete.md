<!--
name: 'System Reminder: Project docs copy to folder incomplete'
description: >-
  Tells Claude that copying the project's text documents into the folder did not
  finish, with the cause and reason.
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_PROJECT_DOCS_COPY_TO_FOLDER_INCOMPLETE_VAR_0
  - SYSTEM_REMINDER_PROJECT_DOCS_COPY_TO_FOLDER_INCOMPLETE_VAR_1
  - SYSTEM_REMINDER_PROJECT_DOCS_COPY_TO_FOLDER_INCOMPLETE_VAR_2
-->
Copying the project's text documents into ${this.deps.folder} did not finish (${SYSTEM_REMINDER_PROJECT_DOCS_COPY_TO_FOLDER_INCOMPLETE_VAR_0}): ${SYSTEM_REMINDER_PROJECT_DOCS_COPY_TO_FOLDER_INCOMPLETE_VAR_1}.${SYSTEM_REMINDER_PROJECT_DOCS_COPY_TO_FOLDER_INCOMPLETE_VAR_2?" The next call that names the folder tries again.":""}
