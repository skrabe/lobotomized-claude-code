<!--
name: 'Tool Description: app_type only TEXT fields'
description: >-
  app_type description: only target text fields; non-text controls refused
  except web dropdowns via 'focused'.
ccVersion: 2.1.330
-->
Only target TEXT fields: typing at a pop-up button, dropdown, or other non-text control is refused (the text would land in whatever field has keyboard focus instead). One exception: a web page's dropdown can be given an option's text with target: 'focused' once app_focus says it holds keyboard focus.
