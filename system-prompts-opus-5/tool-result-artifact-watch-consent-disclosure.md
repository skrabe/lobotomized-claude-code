<!--
name: Artifact watch consent disclosure
description: >-
  Disclosure text for the first artifact-watch permission ask, describing
  republish and comment wakes and their session lifetime.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_CONSENT_DISCLOSURE_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_CONSENT_DISCLOSURE_VAR_1
-->
this session is notified when it is republished elsewhere (another session, or someone saving from the page)${TOOL_RESULT_ARTIFACT_WATCH_CONSENT_DISCLOSURE_VAR_0?" and, if you can edit it and gave its link, comments on it sent to Claude reach this session and Claude may answer them unattended":""}. A local session holds a live background connection; a cloud session is woken with a new turn${TOOL_RESULT_ARTIFACT_WATCH_CONSENT_DISCLOSURE_VAR_1?", also when a comment on any watched artifact is sent to Claude, which Claude may then read and answer":""}. Approving covers watching artifacts for the rest of this session${TOOL_RESULT_ARTIFACT_WATCH_CONSENT_DISCLOSURE_VAR_0?" (turning on auto-replies for another artifact asks again)":""}; republish notifications carry no content
