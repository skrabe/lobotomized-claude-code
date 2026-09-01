<!--
name: 'Skill: Artifact template runtime capabilities note'
description: >-
  Appended to every artifact-template skill body
  (dashboard/report/data-table/explainer) returned as the skill's prompt text,
  telling the model to load the artifact-capabilities skill when the page needs
  more than static HTML
ccVersion: 2.1.239
variables:
  - SKILL_ARTIFACT_TEMPLATE_RUNTIME_CAPABILITIES_NOTE_VAR_0
-->


## When the page needs more than static HTML

This template builds a static page from data in the conversation. If the user wants behavior static HTML cannot provide on its own — the page reading the user's live or connected data, remembering what people do on it (a poll, a sign-up sheet, a checklist, a document edited in place — it saves new versions of itself), keeping state that is shared across viewers, knowing who is viewing, asking Claude a question of its own, storing files people add, or handing the viewer a file to save — that is a runtime capability, granted per user by the control plane: load the \`${SKILL_ARTIFACT_TEMPLATE_RUNTIME_CAPABILITIES_NOTE_VAR_0}\` skill before relying on it.
