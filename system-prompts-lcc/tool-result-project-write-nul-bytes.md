<!--
name: 'Tool Result: project_write content has NUL bytes'
description: project_write refusal when the content contains NUL bytes.
ccVersion: 2.1.291
-->
Write refused; nothing in the project was changed. The content contains NUL bytes, which project docs cannot store (usually a binary or UTF-16 file). Convert it to UTF-8 text (re-encode UTF-16, extract the text from a binary, or remove the NUL bytes), then write again.
