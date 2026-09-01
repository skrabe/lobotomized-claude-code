<!--
name: 'Tool Description: Artifact HTML Skeleton'
description: >-
  Artifact authoring instruction that publish wraps the file in a
  doctype/head/body skeleton, so the model must not emit those tags.
ccVersion: 2.1.257
-->
The file is wrapped in a `<!doctype html>…<head>…</head><body>` skeleton at publish time, so write the page content directly — no `<!DOCTYPE>`, `<html>`, `<head>`, or `<body>` tags of your own. Its head carries only a charset and viewport meta plus a small reset — light `color-scheme`, zero body margin with a 14px system font on an off-white ground, `img{max-width:100%}`, and `[hidden]{display:none!important}` (toggle visibility with `el.hidden`, not `style.display`) — so put your own `<title>` and `<style>` at the top of the file.
