<!--
name: 'Tool Parameter: Bash run_in_background guidance'
description: >-
  Explains Bash run_in_background behavior and that commands do not need a
  trailing ampersand
ccVersion: 2.1.314
variables:
  - ARE_BACKGROUND_SHELLS_KEPT_ELSEWHERE_FN
  - BACKGROUND_TIMEOUT_NOTE_FN
  - BACKGROUND_SHELL_LIFETIME_NOTE_FN
  - BACKGROUND_PERSISTENCE_NOTE_FN
-->
Use `run_in_background` to run the command in the background when you don't need the result immediately; ${ARE_BACKGROUND_SHELLS_KEPT_ELSEWHERE_FN()?"you'll be notified if it finishes while you are still working.":"you'll be notified when it finishes."} No trailing '&' needed.${BACKGROUND_TIMEOUT_NOTE_FN()}${BACKGROUND_SHELL_LIFETIME_NOTE_FN()}${BACKGROUND_PERSISTENCE_NOTE_FN()}
