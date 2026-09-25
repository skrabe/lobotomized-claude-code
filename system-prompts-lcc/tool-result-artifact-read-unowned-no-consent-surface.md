<!--
name: 'Tool Result: Artifact Read — Unowned, No Consent Surface'
description: >-
  Deny message when reading an artifact the user does not own (or whose
  ownership is unconfirmed) needs a person's approval and no one can answer the
  prompt in this session; tells Claude to tell the user in chat.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_ARTIFACT_READ_UNOWNED_NO_CONSENT_SURFACE_VAR_0
-->
${TOOL_RESULT_ARTIFACT_READ_UNOWNED_NO_CONSENT_SURFACE_VAR_0}. Reading content of an artifact the user does not own, or whose ownership couldn't be confirmed, needs a person's yes, and no one can answer the prompt in this session — tell the user in chat instead of retrying.
