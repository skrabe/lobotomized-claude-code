<!--
name: claude-api skill undetected-language read instruction
description: >-
  claude-api skill prompt branch used when no project language was detected and
  skill files were extracted: ask the user which language, then Read the
  matching {lang}/claude-api/README.md from the base directory first.
ccVersion: 2.1.234
-->
No project language was auto-detected. Ask the user which language they are using (see Language Detection above), then Read the matching `{lang}/claude-api/README.md` (or `curl/examples.md` for cURL/raw HTTP or an unsupported language) from the base directory before anything else.
