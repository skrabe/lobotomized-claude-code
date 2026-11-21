<!--
name: 'Tool Result: Computer Use Takeover Declined'
description: >-
  Tool result when the user declines the screen-takeover card, distinct from
  granting background app access.
ccVersion: 2.1.330
-->
The user declined to let this session take over the screen. That's a separate consent from granting an app: approving an app for the background app_* tools does NOT approve a takeover, and request_access can't obtain it. Stay with the app_* tools and tell the user what is left undone; do not try again unless they tell you to.
