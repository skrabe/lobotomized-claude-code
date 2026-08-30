<!--
name: 'Tool Description: Artifact Stateful Pages'
description: >-
  Instructs the model to load the publish-capability skill when building pages
  that save new versions of themselves.
ccVersion: 2.1.246
variables:
  - TOOL_DESCRIPTION_ARTIFACT_STATEFUL_PAGES_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_STATEFUL_PAGES_VAR_1
-->
**Pages that keep their state**: a page this user publishes can save new versions of itself — the artifact publish capability, declared as \`${TOOL_DESCRIPTION_ARTIFACT_STATEFUL_PAGES_VAR_0}\` — so a checklist, tracker, plan, or poll keeps its editors' changes for whoever opens it. If people will change things on the page itself (tick items off, edit entries), or fellow editors should fill it in, build it to save itself; load the \`${TOOL_DESCRIPTION_ARTIFACT_STATEFUL_PAGES_VAR_1}\` skill first for the how-to. A page only read needs none of this.
