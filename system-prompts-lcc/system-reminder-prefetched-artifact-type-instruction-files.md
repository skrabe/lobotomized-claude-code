<!--
name: 'System Reminder: Prefetched Artifact type instruction files'
description: >-
  Reports that an opened Artifact's type instruction files were prefetched to
  disk and directs when to read the Artifact URL or local instruction pages
ccVersion: 2.1.277
variables:
  - PREFETCHED_ARTIFACT_TYPE_FILES
  - ARTIFACT_URL_READ_NOTE
  - ARTIFACT_READ_INCLUDES_TYPE_SKILL
  - TYPE_REFERENCE_PAGE_READ_COMMANDS
-->
The artifact named in this session's opening context was created from its type. These instruction files of its type are already on disk in ${PREFETCHED_ARTIFACT_TYPE_FILES.dir} (saved before this turn; the names below are inside that folder), so do NOT read them with the Artifact tool. The artifact's own content was not read. ${ARTIFACT_URL_READ_NOTE}${ARTIFACT_READ_INCLUDES_TYPE_SKILL?`: SKILL.md comes with that read${TYPE_REFERENCE_PAGE_READ_COMMANDS.length>0?"; the Bash line prints the other pages":""}. If that read's result does not carry the instructions, print SKILL.md from this folder with Bash before you write.`:"; that read's copy of SKILL.md is cut short, so the Bash line prints the whole file too."}
