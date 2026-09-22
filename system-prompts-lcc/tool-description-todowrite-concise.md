<!--
name: 'Tool Description: TodoWrite (concise)'
description: >-
  Concise (velvet) TodoWrite tool description rendered for Opus 4.8 / Fable 5 /
  Mythos 5 — session task list rendered to the user as the working plan
ccVersion: 2.1.177
-->
Create and update a task list for the current session. The list is rendered to the user as your working plan.

- Each todo has `content`, `status` ("pending" | "in_progress" | "completed"), and `activeForm` (present-tense label shown while in progress).
- Send the full list each call; it replaces the previous one.
- Keep one item `in_progress` at a time and mark it `completed` when done.
