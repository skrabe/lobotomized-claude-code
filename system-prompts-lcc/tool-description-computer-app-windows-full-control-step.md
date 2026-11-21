<!--
name: 'Tool Description: Windows request full control per step'
description: >-
  Windows note: use request_full_control for the step, release after; handle
  user_has_app; other virtual desktops usable in place.
ccVersion: 2.1.330
-->
request_full_control for that step and release_full_control after. If a result says the app is the user's active window (user_has_app), ask them to switch to another window and retry. Windows on other virtual desktops can be used in place.
