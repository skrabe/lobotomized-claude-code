<!--
name: 'Tool Description: open_application'
description: >-
  open_application tool description covering background vs display-scope launch
  and the session-allowlist requirement.
ccVersion: 2.1.330
-->
Launch an application (or ensure it's running). In background app mode, the launch does NOT bring it to the front — the user's focus is preserved and the app becomes reachable via the app_* tools. Under full-screen control, the app is brought to the front. The target must already be in the session allowlist — call request_access first.
