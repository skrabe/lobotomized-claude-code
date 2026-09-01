<!--
name: 'Tool Description: Propose Skills (Full)'
description: >-
  Full prompt() body of the propose_skills tool, sent to the model as the tool's
  description with usage rules (max 3 proposals, render-only, no re-proposing).
ccVersion: 2.1.214
-->
Surface recurring multi-step procedures from this session as skill proposals. Render-only: the call shows a review card and the user saves from it; nothing is written.

Call once with all proposals (max 3), when the user asks to turn a workflow into a skill or when the same multi-step procedure has recurred and a skill would clearly save future work. Skip one-off tasks and proposals the user has already seen.
