<!--
name: 'Tool result: app action focus did not follow'
description: >-
  Says keyboard focus did not move into the clicked field and recommends
  app_type with the coordinate (overwrite_existing if the field has text).
ccVersion: 2.1.330
-->
keyboard focus did not move into this field, so the click did not take: keys and typing would still go elsewhere (a field inside a webview behaves this way). To put text here, use app_type with this coordinate: it writes the field's whole value and needs no keyboard focus (overwrite_existing: true if the field has text)
