<!--
name: 'Tool Parameter: Computer action'
description: Action parameter options for the Chrome browser computer tool
ccVersion: 2.0.71
-->
The action to perform:
* `left_click`: Click the left mouse button at the specified coordinates.
* `right_click`: Click the right mouse button at the specified coordinates (context menus).
* `double_click`: Double-click the left mouse button at the specified coordinates.
* `triple_click`: Triple-click the left mouse button to select a line or paragraph.
* `type`: Type a string of text.
* `screenshot`: Take a screenshot of the screen.
* `wait`: Wait a specified number of seconds (rarely needed; most actions auto-wait).
* `scroll`: Scroll up, down, left, or right at the specified coordinates.
* `key`: Press a specific keyboard key.
* `left_click_drag`: Drag from start_coordinate to coordinate (sliders, range selectors, file drag).
* `zoom`: Screenshot a specific region for closer inspection of dense UI.
* `scroll_to`: Scroll an element into view by its reference ID from read_page or find. Prefer over coordinate `scroll` when you have a ref.
* `hover`: Move the cursor to coordinates or an element without clicking, to reveal tooltips, dropdowns, or hover states.
