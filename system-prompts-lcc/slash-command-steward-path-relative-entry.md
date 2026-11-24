<!--
name: 'Slash Command: Steward PATH relative entry'
description: 'Steward refusal when a PATH entry is empty, ''.'', ''~'' or relative'
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_0
  - SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_1
  - SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_2
  - SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_3
  - SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_4
  - SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_5
-->
entry ${SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_0+1} of ${SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_1.length} on your PATH${SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_2.length>1?` (and ${SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_2.length-1} more)`:""} ${SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_3===""?"is empty (a stray colon), which stands for the current folder":SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_3==="."?'is ".", the current folder':SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_3.startsWith("~")?'begins with "~", which only a shell expands':"is a relative path, which changes with the current folder"}, so it isn't clear which gh and git ${SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_4?"an unattended watch ":""}would run. Take ${SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_2.length>1?"them":"it"} out${SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_2.every((SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_5)=>SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_1[SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_5]==="")?" of your shell's profile, and out of":`, or write ${SLASH_COMMAND_STEWARD_PATH_RELATIVE_ENTRY_VAR_2.length>1?"them as full paths":"it as a full path"}, in your shell's profile, and in`} Claude Code's settings if an env block there sets PATH, then quit Claude Code and start it again from a new terminal
