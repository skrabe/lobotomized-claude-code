<!--
name: 'Skill: Code review findings fixed later'
description: >-
  Code-review note telling the model to re-report findings with outcomes the
  moment they get fixed later in the session.
ccVersion: 2.1.218
variables:
  - SKILL_CODE_REVIEW_FINDINGS_FIXED_LATER_VAR_0
-->


## If findings are fixed later

Whenever reported findings get fixed later in this session - the user asks you
to fix them, or later work fixes them incidentally - you MUST ${SKILL_CODE_REVIEW_FINDINGS_FIXED_LATER_VAR_0}.
Make that call immediately after the fixes land, before any prose summary; the
host UI's per-finding status updates only from it, and without it the findings
stay marked unresolved.
