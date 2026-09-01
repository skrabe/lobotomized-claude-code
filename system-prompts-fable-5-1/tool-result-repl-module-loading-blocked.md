<!--
name: REPL module loading blocked
description: >-
  Error returned to the model from the REPL when its code tries to load a
  module; advises using tool globals.
ccVersion: 2.1.206
-->
Use the tool globals instead: await Read({file_path: '...'}), await Glob({pattern: '...'}), the registered shell tool, etc.
