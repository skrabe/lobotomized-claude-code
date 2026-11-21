<!--
name: 'Tool Description: Computer app_release'
description: >-
  Description of the app_release tool: releases this session's hold on
  application windows (captures forgotten), when to call it, and how
  app/window_id scope the release.
ccVersion: 2.1.330
-->
Release this session's hold on application windows; their captures are forgotten too. No release is needed between applications. Call it where a refusal asks for it, or when you are done with every application: while this session holds a window, other Claude sessions cannot capture it or act on it. Pass `app` (its bundle identifier, and `window_id`) for one; no arguments for all.
