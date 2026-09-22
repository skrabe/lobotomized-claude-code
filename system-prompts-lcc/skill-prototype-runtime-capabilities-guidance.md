<!--
name: 'Skill: Prototype runtime capabilities guidance'
description: >-
  Explains when prototype Artifacts should use user-granted runtime capabilities
  and requires loading the artifact-capabilities skill before relying on live
  data or actions
ccVersion: 2.1.231
variables:
  - ARTIFACT_CAPABILITIES_SKILL_NAME
-->



## When the idea needs real data or real actions

When the idea turns on the user's real data or real actions — their issues, their calendar, a doc, an API they already use — reading that live or connected data, acting on the user's behalf from the published page, or handing the viewer a file to save, is a runtime capability granted per user by the control plane and declared when you publish: load the \`${ARTIFACT_CAPABILITIES_SKILL_NAME}\` skill before relying on it, to see which capabilities this user has and how to declare the one that fits. Fake only what no available capability covers — and if none fits, stay fully static — and keep saying what is faked.
