<!--
name: Tool Parameter JSON Single-Value Rule
description: >-
  Model-facing tool_param_json system-prompt block (e2m) instructing that
  object/array parameter values must be a single JSON value and never contain
  parameter-tag markup; conditionally injected (uwi() or tengu_silent_harbor
  gate).
ccVersion: 2.1.191
-->
Object and array parameter values must be a single JSON value — never write parameter-tag markup inside a JSON value.
