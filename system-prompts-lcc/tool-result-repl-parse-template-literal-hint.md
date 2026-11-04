<!--
name: 'Tool Result: REPL parse template literal hint'
description: >-
  Hint that backticks and ${ in template literals break text, suggesting quoted
  strings or files
ccVersion: 2.1.318
-->
A template literal ends at the next backtick and `${` starts an interpolation, so text that contains either (RST ``code``, a shell ${VAR}, a Python f-string) is safer in a '…' or "…" string, or read from a file.
