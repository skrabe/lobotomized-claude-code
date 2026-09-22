<!--
name: 'Tool Description: Propose Skills (Full)'
description: >-
  Full prompt() body of the propose_skills tool, sent to the model as the tool's
  description with usage rules (max 3 proposals, render-only, no re-proposing).
ccVersion: 2.1.274
-->
Surface recurring multi-step procedures from this session as skill proposals. Render-only: the call shows a review card and the user saves from it; nothing is written. A saved proposal replaces the whole skill, so an improvement carries the complete updated SKILL.md, not a partial edit.

Call once with all proposals (max 3), when the user asks to turn a workflow into a skill or when the same multi-step procedure has recurred and a skill would clearly save future work. Skip one-off tasks and proposals the user has already seen.

An improvement can only update one of the user's own skills; a plugin's skill or a built-in one can't be updated from the card. To customize one of those with this tool, propose it as a new skill under a name of its own — not the original's name, even without its plugin prefix — with a description that says when to use it instead of the original: both stay listed, and the description decides which one is used.
