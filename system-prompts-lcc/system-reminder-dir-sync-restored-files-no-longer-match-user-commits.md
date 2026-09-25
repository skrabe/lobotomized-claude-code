<!--
name: 'System Reminder: Dir-sync restored files no longer match user commits'
description: >-
  Dir-sync notice suffix listing files whose rewound or rewritten content no
  longer matches the user's restored commits. It tells the model to check git
  diff and restore with git checkout HEAD unless undoing those commits was
  intended.
ccVersion: 2.1.282
variables:
  - SYSTEM_REMINDER_DIR_SYNC_RESTORED_FILES_NO_LONGER_MATCH_USER_COMMITS_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_RESTORED_FILES_NO_LONGER_MATCH_USER_COMMITS_VAR_1
-->
 These files no longer match the user's commits — your rewound version or your rewrite — here and, as uncommitted changes, on the user's machine: ${SYSTEM_REMINDER_DIR_SYNC_RESTORED_FILES_NO_LONGER_MATCH_USER_COMMITS_VAR_0(SYSTEM_REMINDER_DIR_SYNC_RESTORED_FILES_NO_LONGER_MATCH_USER_COMMITS_VAR_1.restored.files,{openEnded:SYSTEM_REMINDER_DIR_SYNC_RESTORED_FILES_NO_LONGER_MATCH_USER_COMMITS_VAR_1.restored.filesTruncated,show:Bo})}. Check \`git diff HEAD -- PATH\` first (the user may have uncommitted edits of their own there); then \`git checkout HEAD -- PATH\` puts the user's committed version back (for a file those commits deleted, remove it instead), unless undoing those commits is what the user asked for.
