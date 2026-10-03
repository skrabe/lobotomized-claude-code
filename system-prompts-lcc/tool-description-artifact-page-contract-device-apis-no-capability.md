<!--
name: 'Tool Description: Artifact Page Contract Device APIs No Capability'
description: >-
  Rewritten page-contract paragraph for sessions without the capability skill:
  camera, microphone, screen capture, location and Web Share are refused without
  a prompt, so take such input as uploaded files.
ccVersion: 2.1.288
-->
Camera, microphone, screen capture, location, Web Share and similar device APIs are refused without a prompt — don't build features on them (a screen wake lock may be granted while the page is visible: request it and tolerate rejection); file inputs, drag-and-drop of files and `FileReader` work in browsers, so take photos, audio and data as uploaded files instead.
