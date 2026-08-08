<!--
name: 'Tool Parameter: memory_write content'
description: >-
  Input-schema description of the memory_write tool's `content` parameter,
  spelling out whole-document replacement, normalization, and the 100KB cap.
ccVersion: 2.1.224
-->
Full text content to write (UTF-8). Replaces the entire document — any line you omit is deleted. Line endings are normalized to LF, invisible/format characters are stripped, and other control characters are replaced with U+FFFD. Empty or whitespace-only content is rejected. Capped at 100KB per document.
