<!--
name: 'Tool Result: Design finalize_plan scope "project" Unsupported'
description: >-
  ClaudeDesign permission-deny message returned to the model when finalize_plan
  is called with scope "project", directing it to write directly or use
  path-scoped writes/deletes plans.
ccVersion: 2.1.211
-->
ClaudeDesign finalize_plan: scope "project" is no longer supported by this client. Write files directly without plan_token — the first write to a project asks for a one-time durable approval — or use finalize_plan with writes/deletes for path-scoped plans and deletes.
