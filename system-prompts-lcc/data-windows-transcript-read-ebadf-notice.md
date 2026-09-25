<!--
name: 'Data: Windows transcript read EBADF notice'
description: >-
  Explains a Windows-only EBADF error reading the session transcript file likely
  caused by security or endpoint-management software intercepting file reads,
  and suggests excluding the .claude folder or allow-listing Claude Code before
  resuming
ccVersion: 2.1.282
-->
Windows reported an error (EBADF) when Claude Code read this session's transcript file, although the file had opened normally. This can happen when other software intercepts file reads — security, encryption or endpoint-management tools, for example. If it keeps happening for this conversation, try excluding the folder that holds Claude Code's session transcripts from such software (the .claude folder in your user profile, unless the app or CLAUDE_CONFIG_DIR points Claude Code elsewhere), or adding Claude Code to its allowed applications, then resume again.
