<!--
name: 'Tool Result: hearthbot MCP Policy Arguments Refused'
description: >-
  Error thrown by the MCP fetch wrapper when a hearthbot call carries arguments
  the organization's MCP policy doesn't allow (project_id, unlisted args).
ccVersion: 2.1.330
-->
Under your organization's MCP policy hearthbot serves only Claude's answers, reads of this Project and thread starts in it. Leave project_id out of any call, and leave out of a read or a thread start every argument that its schema does not list (device and computer among them).
