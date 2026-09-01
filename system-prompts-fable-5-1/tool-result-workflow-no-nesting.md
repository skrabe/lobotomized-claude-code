<!--
name: Workflow no-nesting error
description: >-
  Error returned to the workflow-authoring model when its script calls
  workflow() inside a child workflow.
ccVersion: 2.1.206
-->
workflow() cannot be called from within a child workflow — nesting is limited to one level. Inline the inner script or call its agents directly.
