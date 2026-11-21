<!--
name: 'Tool result: Permission deny rm-guard folder'
description: Denial when file tools would write to the config dir rm-guard folder
ccVersion: 2.1.330
-->
Claude Code's file tools do not write to the rm-guard folder of the Claude Code config directory ($CLAUDE_CONFIG_DIR or ~/.claude), or through a link into it: on a hosted worker, a script there runs in place of rm. Write the file somewhere else.
