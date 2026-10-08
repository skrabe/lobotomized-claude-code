<!--
name: Project write new document retry advice
description: Advises reading back a possibly saved new document before limited retries.
ccVersion: 2.1.294
-->
 Call project_read on this path: if it returns the content, the save went through late; if not, try the same project_write again, up to two retries in total. If it still fails, tell the user that it was not saved, and offer it to them another way.
