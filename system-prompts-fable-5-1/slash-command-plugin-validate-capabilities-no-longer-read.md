<!--
name: 'Slash Command: /plugin validate — capabilities field no longer read'
description: >-
  Validation error telling the user to delete plugin.json's capabilities field
  because hooks are discovered from source and listed under hooks.json.
ccVersion: 2.1.246
-->
'capabilities' is no longer read: what a hooks module hooks and calls on $ is read from its source and listed under its hooks.json below. Delete the field.
