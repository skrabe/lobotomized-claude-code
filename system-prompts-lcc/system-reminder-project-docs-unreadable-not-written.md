<!--
name: 'System Reminder: Project docs unreadable, not written'
description: >-
  Tells Claude how many of the project's text documents could not be read and so
  were not written to the folder.
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_PROJECT_DOCS_UNREADABLE_NOT_WRITTEN_VAR_0
  - SYSTEM_REMINDER_PROJECT_DOCS_UNREADABLE_NOT_WRITTEN_VAR_1
-->
${SYSTEM_REMINDER_PROJECT_DOCS_UNREADABLE_NOT_WRITTEN_VAR_0.docs} of the project's ${SYSTEM_REMINDER_PROJECT_DOCS_UNREADABLE_NOT_WRITTEN_VAR_0.of} text ${SYSTEM_REMINDER_PROJECT_DOCS_UNREADABLE_NOT_WRITTEN_VAR_1(SYSTEM_REMINDER_PROJECT_DOCS_UNREADABLE_NOT_WRITTEN_VAR_0.of,"document")} could not be read, so ${SYSTEM_REMINDER_PROJECT_DOCS_UNREADABLE_NOT_WRITTEN_VAR_1(SYSTEM_REMINDER_PROJECT_DOCS_UNREADABLE_NOT_WRITTEN_VAR_0.docs,"it was","they were")} not written to ${this.deps.folder}.
