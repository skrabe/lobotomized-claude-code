<!--
name: 'Tool Description: Computer app_screenshot returns'
description: >-
  app_screenshot description: returned image, element summary, coordinate frame,
  other apps
ccVersion: 2.1.330
-->
Returns the image plus a compact summary of interactive elements (role, position, title) within the window. The (x, y) coordinates you pass to app_click etc. are ALWAYS pixels in this screenshot's full-resolution coordinate frame (reported with every scaled app_screenshot; equal to the image's pixels for unscaled ones). To see what another granted application shows, capture that application with app_screenshot; use app_list_windows for its windows. A full-screen screenshot shows no window of an application that is not granted.
