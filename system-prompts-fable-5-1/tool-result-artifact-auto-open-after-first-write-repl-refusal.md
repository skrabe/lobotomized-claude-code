<!--
name: 'Tool Result: Artifact auto_open after_first_write REPL refusal'
description: >-
  Refuses after_first_write auto_open when AppifactRepl would fill the Artifact,
  because REPL writes never open the page.
ccVersion: 2.1.273
-->
`auto_open`: "after_first_write" waits for a write made with this tool (`write_db`, or a files publish); a fill through the AppifactRepl tool never opens the page, so it would stay closed. Nothing was created. Retry this same create without `auto_open`: the Artifact opens as soon as it is created, and the REPL's writes paint in front of the user.
