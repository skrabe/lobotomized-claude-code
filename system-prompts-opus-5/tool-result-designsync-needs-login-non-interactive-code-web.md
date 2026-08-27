<!--
name: 'Tool Result: DesignSync Needs Login Non-Interactive Code Web'
description: >-
  DesignSync needs_design_login error for non-interactive sessions, including
  the claude.ai/code Send-to-Claude-Code-Web remedy.
ccVersion: 2.1.247
-->
DesignSync needs design-system authorization, and /design-login cannot run in this non-interactive session. Ask the user to run /design-login once from an interactive Claude Code session on this machine — headless and SDK runs here then reuse that authorization. If this is claude.ai/code, ask them instead to use Claude Design's "Send to Claude Code Web" (which seeds the project into the workspace) or to provide the project files directly.
