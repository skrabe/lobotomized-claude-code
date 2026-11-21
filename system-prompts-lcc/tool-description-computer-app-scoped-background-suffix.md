<!--
name: 'Tool Description: Computer App-Scoped Background Suffix'
description: >-
  Shared suffix on app_* tool descriptions stating they act in the background
  and when display-scope tools are still required.
ccVersion: 2.1.330
-->


This tool acts on one application in the BACKGROUND while the user keeps working in other apps. The target window does not come to the front. For the menu bar use app_menu. `app` says which application a call acts on. To act in another granted application, call the app_* tools with that application; no release is needed in between. When you come back to an application, take a fresh app_screenshot first: a coordinate or an element_index points at a place in the capture it came from, not at an element.
