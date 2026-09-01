<!--
name: 'Tool Parameter: SendMessage summary preview'
description: >-
  Description of SendMessage's `summary` parameter; reworded from the 2.1.221 id
  to add the truncation-not-rejection and first-line-only behaviour.
ccVersion: 2.1.227
variables:
  - TOOL_PARAMETER_SENDMESSAGE_SUMMARY_PREVIEW_VAR_0
-->
A 5-10 word summary shown as a one-line preview in the UI. Defaults to the first line of a plain-text message; longer summaries are truncated to ${TOOL_PARAMETER_SENDMESSAGE_SUMMARY_PREVIEW_VAR_0} characters rather than rejected.
