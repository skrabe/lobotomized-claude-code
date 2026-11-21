<!--
name: 'App action: key cannot be aimed'
description: >-
  Refusal: key needs real keystroke that element_index cannot aim; click first
  then send without index.
ccVersion: 2.1.330
-->
accessibility could not deliver this key here, and the only other way is a real keystroke, which goes to whatever holds keyboard focus: an element_index cannot aim it. No keystroke was sent. app_click the element by its element_index first (a click moves keyboard focus there), check a fresh app_screenshot, then send the key without element_index
