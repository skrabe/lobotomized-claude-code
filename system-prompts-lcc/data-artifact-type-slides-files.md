<!--
name: 'Data: Artifact type slides files'
description: Lists the files a slides artifact keeps under project/
ccVersion: 2.1.326
-->
`project/deck.css` when `format` lists it, plain CSS holding the rules and `--variables` every slide shares, and one `project/slides/<id>.html` per slide, <id> being its entry in the index's `order`, each holding exactly one `<section id="<id>">` in the slide format with, as that section's last child, one `<aside>` of plain-text speaker notes when the slide has any
