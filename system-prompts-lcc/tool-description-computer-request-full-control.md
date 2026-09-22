<!--
name: Request Full Control Description
description: >-
  Description of request_full_control asking the model to request session-wide
  display-scope approval.
ccVersion: 2.1.246
-->
Ask the user to approve full-screen control (screenshot, left_click, type, ...) for THIS SESSION. Use this when a background app_* action returned that taking over the screen needs approval. Once approved, the display-scope tools work for the rest of the session; you do not need to call this again.
