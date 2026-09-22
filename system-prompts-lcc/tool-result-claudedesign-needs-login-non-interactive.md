<!--
name: 'Tool Result: ClaudeDesign Needs Login Non-Interactive'
description: >-
  Claude Design needs_design_login error when /design login cannot run in a
  non-interactive session.
ccVersion: 2.1.247
-->
Claude Design needs a claude.ai credential, and /design login cannot run in this non-interactive session. Ask the user to run /design login once from an interactive Claude Code session on this machine — non-interactive runs here then reuse that authorization. (CI runners and hosted sessions have no interactive session; Claude Design is not reachable from those without a stored /design login credential.)
