<!--
name: 'Tool Description: Artifact calls document skeleton and assets'
description: >-
  Rewrite replacement on document skeleton wrapping and uploading assets with
  url and asset true
ccVersion: 2.1.330
-->
is served at to its source. Only the page is wrapped in a document skeleton: an HTML file in `files` starts with its own `<!doctype html>`, charset and viewport. With `url` and `asset: true` it uploads files to an artifact whose page declares `assets`; Claude uses each returned url exactly as given.
