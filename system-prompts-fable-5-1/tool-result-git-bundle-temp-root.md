<!--
name: 'Tool Result: Git Bundle Temp Root'
description: >-
  Refuses the upload when the checkout stands under cloud-session scratch space
  so its contents cannot be told apart from session writes.
ccVersion: 2.1.247
-->
Not uploading this working tree: this checkout stands — or a link on the way to it leads — under a directory cloud sessions on this machine use as scratch space, so nothing in it can be told apart from what such a session put there. Start from the checkout at its ordinary location instead.
