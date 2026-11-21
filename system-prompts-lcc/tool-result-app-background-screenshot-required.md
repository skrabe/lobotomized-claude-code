<!--
name: 'App tools: background screenshot required'
description: Refusal when acting on a background window without a current app_screenshot.
ccVersion: 2.1.330
-->
Acting on a window in the background requires a current app_screenshot of that window, and there is none (none taken yet, or it was dropped by app_release). Take an app_screenshot of this window (pass window_id if it is not the app's default window), then retry.
