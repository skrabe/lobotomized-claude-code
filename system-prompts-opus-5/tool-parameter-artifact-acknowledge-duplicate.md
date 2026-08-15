<!--
name: 'Tool Parameter: Artifact acknowledge_duplicate'
description: >-
  Schema description for the Artifact tool acknowledge_duplicate parameter,
  permitting a reply when one already stands and warning that it is only for a
  deliberate follow-up that adds something new
ccVersion: 2.1.233
-->
reply only: post even though a Claude reply already stands after every "sent to Claude" request on the thread. Without it such a reply is refused as a likely duplicate. Pass true only for a deliberate follow-up that adds something new — never to restate what the standing reply said.
