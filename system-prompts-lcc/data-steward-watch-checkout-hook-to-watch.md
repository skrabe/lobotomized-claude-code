<!--
name: 'Data: Steward watch checkout hook remedy'
description: >-
  How to restore a /steward watch blocked by a checkout settings hook: remove it
  or narrow its matcher, copying it to user settings only if read
ccVersion: 2.1.330
variables:
  - DATA_STEWARD_WATCH_CHECKOUT_HOOK_TO_WATCH_VAR_0
  - DATA_STEWARD_WATCH_CHECKOUT_HOOK_TO_WATCH_VAR_1
  - DATA_STEWARD_WATCH_CHECKOUT_HOOK_TO_WATCH_VAR_2
-->
To watch, take the hook out of ${DATA_STEWARD_WATCH_CHECKOUT_HOOK_TO_WATCH_VAR_0?.DATA_STEWARD_WATCH_CHECKOUT_HOOK_TO_WATCH_VAR_1??"this checkout's settings"}${DATA_STEWARD_WATCH_CHECKOUT_HOOK_TO_WATCH_VAR_2?", in the folder that Claude Code runs in":""}, or set its matcher to other tools.${DATA_STEWARD_WATCH_CHECKOUT_HOOK_TO_WATCH_VAR_2?" If your team shares this file, that turns their check off for you and leaves the file changed. A watch won't commit that change.":""} Copy the hook to your own settings, where it runs in every project, only if you have read what it runs, and keep its script outside any checkout
