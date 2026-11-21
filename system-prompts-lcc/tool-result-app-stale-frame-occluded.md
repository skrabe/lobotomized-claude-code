<!--
name: 'App tools: stale frame occluded'
description: >-
  Refusal when the last app_screenshot is flagged stale because the window is
  covered.
ccVersion: 2.1.330
-->
The last app_screenshot of this window was flagged as possibly STALE (the window is fully covered and this app stops redrawing while covered), so acting on it is refused. Ask the user to leave part of the window visible, take a fresh app_screenshot, and retry once it is no longer flagged.
