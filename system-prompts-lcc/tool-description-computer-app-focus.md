<!--
name: 'Tool Description: Computer app_focus'
description: >-
  app_focus tool description: give keyboard focus without clicking, limits and
  refusals
ccVersion: 2.1.330
-->
Give keyboard focus to an element in one window of a granted application WITHOUT clicking it and without bringing the app to the front. Use it to aim the next coordinate-less app_type/app_key at a specific field in the window that already holds the app's text cursor. It cannot pull the text cursor into a different window of the app: in that case it answers that focus did not move, and app_click on the element is the way in. With no coordinate or element_index it aims at your last action point in this window, like the other app_* tools. The focus stays where you put it (it is not restored). Refused while the user is working in that app (it is frontmost), for elements inside a dialog sheet or while an Open/Save panel holds the app's focus, and for password fields.
