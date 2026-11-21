<!--
name: 'App action: text cannot be aimed'
description: >-
  Refusal: text needs real typing that element_index cannot aim; click first
  then app_type without index.
ccVersion: 2.1.330
-->
accessibility could not write the text here, and the only other way is real typing, which goes to whatever holds keyboard focus: an element_index cannot aim it. No keystrokes were sent. app_click the field by its element_index first (a click moves keyboard focus there), check a fresh app_screenshot, then call app_type without element_index
