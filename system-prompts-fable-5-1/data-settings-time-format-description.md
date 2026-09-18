<!--
name: 'Data: timeFormat setting description'
description: >-
  Description of the `timeFormat` setting in Claude Code's settings JSON schema.
  The model reads it through /update-config and settings validation errors; it
  is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Clock format for times shown in the UI: "auto" (default, follows the locale), "12-hour", "24-hour", "24-hour-utc" ("18:05Z"), or a strftime pattern such as "%H:%M" (any value containing "%"; other values read as "auto"). A pattern replaces the time everywhere; message timestamps show only the pattern, so include %Y-%m-%d for the date. /config offers the presets; a pattern is set here.
