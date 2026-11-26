<!--
name: 'System Reminder: Staged files disk-space recovery'
description: >-
  Explains recovery after staged file copies run out of disk space,
  distinguishing connector downloads that can be fetched again from files that
  must be reattached or recreated
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_0
  - SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_1
  - SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_2
  - CONNECTOR_DOWNLOADS_PATH_PREFIX
  - SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_4
  - BROWSER_DOWNLOADS_PATH_PREFIX
  - SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_6
  - SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_7
-->

At least one of these copies failed with "no space left on device". ${SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_0===SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_1.length?`Make space. Then read ${SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_1.length===1?"that file":"each file"} again, which can fetch it again. If it is still missing after a minute, run the connector's tool again, but ask the user first if that tool changes anything. Do not ask the user to attach it.`:`That file is not sent again by itself. Make space.${SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_2?" Then ask the user to attach it, or make it again if you made it.":""}${SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_0>0?` ${SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_2?"But":"Then"} read a file under ${CONNECTOR_DOWNLOADS_PATH_PREFIX} again, which can fetch it again. If it is still missing after a minute, run the connector's tool again, but ask the user first if that tool changes anything. Do not ask the user to attach it.`:""}${SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_4>0?` ${SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_2||SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_0>0?"But":"Then"} save a file under ${BROWSER_DOWNLOADS_PATH_PREFIX} again with the cloud browser's save tool, if the browser's list of downloads still has it, or else download it from the site again. The new copy gets a new name. Do not ask the user to attach it.`:""}${SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_6>0?` ${SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_4>0?"And":SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_2||SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_0>0?"But":"Then"} download a file under ${SYSTEM_REMINDER_STAGED_FILES_DISK_SPACE_RECOVERY_VAR_7} from its site again in the desktop app's browser, and save it again with that browser's save_download tool. The new copy gets a new name. Do not ask the user to attach it.`:""}`} Ask the user before you delete one of their files.
