<!--
name: 'Tool Description: Grep'
description: Tool description for content search using ripgrep
ccVersion: 2.1.218
variables:
  - GREP_TOOL_NAME
  - BASH_TOOL_NAME
  - AGENT_TOOL_NAME
-->

Search file contents with ripgrep.

Usage:
- Supports full regex syntax (e.g. "log.*Error", "function\\s+\\w+").
- Filter files with the glob parameter (e.g. "*.js", "**/*.tsx") or type parameter (e.g. "js", "py", "rust").
- Output modes: "content" (matching lines), "files_with_matches" (paths only, default), "count" (match counts).
- Pattern syntax uses ripgrep (not grep): literal braces need escaping (`interface\\{\\}` to find `interface{}` in Go).
- Patterns match within single lines by default; for cross-line patterns (e.g. `struct \\{[\\s\\S]*?field`) set `multiline: true`.
