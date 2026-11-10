<!--
name: 'Permission ask: ClaudeDesign project write grant'
description: >-
  Approval message for granting durable write access to a ClaudeDesign project;
  becomes the tool_result on decline.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_DESIGN_PROJECT_WRITE_GRANT_APPROVAL_VAR_0
-->
Approving writes the listed files now, and lets Claude write to ANY file in the project "${TOOL_RESULT_DESIGN_PROJECT_WRITE_GRANT_APPROVAL_VAR_0.name}" (${TOOL_RESULT_DESIGN_PROJECT_WRITE_GRANT_APPROVAL_VAR_0.sharingLabel}) — ${TOOL_RESULT_DESIGN_PROJECT_WRITE_GRANT_APPROVAL_VAR_0.url} — without asking again. This approval is remembered for this project until you revoke it in settings at claude.ai/design (future writes and file contents are not shown for approval). Deletes and CLAUDE.md, CLAUDE.local.md and .claude paths still ask every time.
