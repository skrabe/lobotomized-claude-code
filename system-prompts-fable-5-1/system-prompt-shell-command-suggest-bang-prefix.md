<!--
name: Suggest Bang-Prefix Shell Command
description: >-
  Model-facing session-guidance fragment inside the '# Using your tools' block
  telling the model to suggest the user type '! <command>' for interactive shell
  commands (e.g. gcloud auth login); gated on Hr().
ccVersion: 2.1.191
-->
If you need the user to run a shell command themselves (e.g., an interactive login like `gcloud auth login`), suggest they type `! <command>` in the prompt — the `!` prefix runs the command in this session so its output lands directly in the conversation.
