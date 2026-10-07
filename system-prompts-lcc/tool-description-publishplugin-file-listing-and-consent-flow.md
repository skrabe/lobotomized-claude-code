<!--
name: 'Tool Description: PublishPlugin file listing and consent flow'
description: >-
  Explains that PublishPlugin lists the plugin's own files, shows the person the
  folder, organization, count, size and file names, sends nothing before their
  yes in any permission mode, and writes a manifest first for folders without
  one
ccVersion: 2.1.292
-->
The tool lists the plugin's own files (what `.gitignore` names, secrets, links, `.git` and installed packages stay on the machine), shows the person the folder, the organization, the count and size and the files by name (past twenty, the rest counted), and asks them. Nothing is sent before their yes, in any permission mode; where nobody can be asked, the tool refuses. For a folder with no manifest it writes one first (a name from the folder, version 0.1.0, your `description`), shown in full in the same question.
