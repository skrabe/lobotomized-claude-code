<!--
name: 'Skill: Artifact template runtime capabilities note'
description: >-
  Appended to every artifact-template skill body
  (dashboard/report/data-table/explainer) returned as the skill's prompt text,
  telling the model to load the artifact-capabilities skill when the page needs
  more than static HTML
ccVersion: 2.1.231
variables:
  - SKILL_ARTIFACT_TEMPLATE_RUNTIME_CAPABILITIES_NOTE_VAR_0
-->


## When the page needs more than static HTML

This template builds a static page from data in the conversation. If the user wants behavior static HTML cannot provide on its own — the page reading the user's live or connected data, keeping state that is shared across viewers, handing the viewer a file to save, or updating and republishing itself — that is a runtime capability, granted per user by the control plane: load the \`${SKILL_ARTIFACT_TEMPLATE_RUNTIME_CAPABILITIES_NOTE_VAR_0}\` skill before relying on it.
