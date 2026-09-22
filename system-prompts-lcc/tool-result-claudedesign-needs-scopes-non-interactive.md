<!--
name: 'Tool Result: ClaudeDesign Needs Scopes Non-Interactive'
description: >-
  DesignNeedsScopesError when a 403 needs_design_scopes response arrives in a
  non-interactive session.
ccVersion: 2.1.247
-->
Claude Design rejected this session's claude.ai credential (HTTP 403): it does not carry Claude Design access, and /design login cannot run in this non-interactive session. Ask the user to run /design login once from an interactive Claude Code session on this machine — non-interactive runs here then reuse that authorization. (CI runners and hosted sessions have no interactive session; Claude Design is not reachable from those without a stored /design login credential.)
