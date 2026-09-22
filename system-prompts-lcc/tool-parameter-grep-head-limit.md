<!--
name: 'Tool Parameter: Grep head_limit'
description: >-
  The head_limit param in the Grep tool input schema limiting output to first N
  lines/entries; model-facing.
ccVersion: 2.1.191
-->
Limit output to first N lines/entries, equivalent to "| head -N". Works across all output modes: content (limits output lines), files_with_matches (limits file paths), count (limits count entries). Defaults to 250 when unspecified. Pass 0 for unlimited (use sparingly — large result sets waste context).
