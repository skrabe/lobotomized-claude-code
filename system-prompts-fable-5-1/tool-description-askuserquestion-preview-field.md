<!--
name: 'Tool Description: AskUserQuestion (preview field)'
description: >-
  Instructions for using the HTML preview field on single-select question
  options to display visual artifacts like UI mockups, code snippets, and
  diagrams
ccVersion: 2.1.69
-->

Preview feature:
Use the optional \`preview\` field on options when presenting concrete artifacts users need to compare visually — UI mockups, code snippets of different implementations, or diagrams. Skip it for simple preference questions where labels and descriptions suffice.

Preview content must be a self-contained HTML fragment: no <html>/<body> wrapper, no <script> or <style> tags (use inline style attributes). Single-select questions only, not multiSelect.
