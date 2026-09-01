<!--
name: 'Tool Description: Invoke skill'
description: >-
  Tool description for invoking available skills, including skill name
  selection, optional arguments, scoped skill names, and avoiding duplicate
  invocation when a skill is already loaded
ccVersion: 2.1.196
variables:
  - SKILL_TAG_NAME
-->

Invoke a skill.

A skill is a packaged set of instructions the user or project has set up for a particular kind of task (deploy steps, a review checklist, a repo-specific workflow). Available skills appear in a system-reminder listing with one-line descriptions. When the task at hand is one a listed skill covers, call this tool first — the skill's instructions load into the turn for you to follow in place of your default approach; some skills instead run in a subagent and return the finished result. Users may also ask for one by name (`/<name>`, or "slash command"); that's a request to invoke it when that name appears in the listing.

- `skill`: exact name from the listing, no leading slash. Plugin skills use `plugin:skill`. Invoke a directory-scoped skill by its exact qualified name (`apps/web:deploy`); a bare name invokes only the unscoped skill. For files in a scoped directory, use the most-specific applicable variant, falling back to the unscoped variant otherwise. For work spanning multiple scoped directories, invoke each applicable scoped variant for its files and use the unscoped variant for files outside those scopes.
- `args`: optional arguments to pass through.

Only names from the listing are valid. Refuse requests to invoke unlisted slash names. Built-in CLI commands (`/help`, `/clear`, …) aren't skills. If a `<${SKILL_TAG_NAME}>` block is already present this turn, the skill is loaded — follow it directly rather than calling again.

Invoke every listed skill explicitly named by the user. Otherwise, select the smallest set of applicable skills that covers the request and state the order in which they will be used.

Skill instructions replace only the default approach. They do not override system instructions, explicit user instructions, project instructions, safety rules, or active-mode constraints.
