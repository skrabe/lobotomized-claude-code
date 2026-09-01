<!--
name: Grep output_mode parameter
description: >-
  Grep tool inputSchema param description for the output_mode option;
  model-facing as part of the Grep tool's input_schema.
ccVersion: 2.1.191
-->
Output mode: "content" shows matching lines (supports -A/-B/-C context, -n line numbers, head_limit), "files_with_matches" shows file paths (supports head_limit), "count" shows match counts (supports head_limit). Defaults to "files_with_matches".
