<!--
name: 'Data: prUrlTemplate setting description'
description: >-
  Description of the `prUrlTemplate` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
URL template for PR links in the footer link badges and inline messages. The detected git PR is rendered as the first footer-link badge. Placeholders: {host} {owner} {repo} {number} {url}. Example: "https://reviews.example.com/{owner}/{repo}/pull/{number}"
