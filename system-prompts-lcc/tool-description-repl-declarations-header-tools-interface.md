<!--
name: 'Tool Description: REPL declarations header with Tools interface'
description: >-
  Declarations header explaining interface Tools, cut doc lines, describeTool
  and searchTools
ccVersion: 2.1.318
-->
// The globals of a REPL script, as TypeScript declarations. interface Tools covers the built-in tools a script can call that aren't in your tool list; long doc lines are cut short, and describeTool(name) returns a tool's description and full input schema. searchTools finds the others, such as MCP tools.
