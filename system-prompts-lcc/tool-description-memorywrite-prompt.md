<!--
name: 'Tool Description: MemoryWrite'
description: >-
  The MemoryWrite tool description: writing a full memory document to a
  connected store, and the if_version contract that stops the model overwriting
  content it hasn't read.
ccVersion: 2.1.246
variables:
  - MEMORY_LIST_TOOL_NAME
  - MEMORY_READ_TOOL_NAME
  - MEMORY_WRITE_TOOL_NAME
-->
Create or update a memory document with full content, in the memory store named by store (call ${MEMORY_LIST_TOOL_NAME} with no arguments to see the stores available in this session). Overwrites if the path already exists: content replaces the ENTIRE document — this is not an append or a patch. Include every existing line you intend to keep; any line you omit is deleted. Use this to save durable knowledge about the project and how to work in it — not transient task state. Always pass if_version: the version token from your most recent ${MEMORY_READ_TOOL_NAME} or ${MEMORY_WRITE_TOOL_NAME} of this path, or the literal word new (without quotes) for a file that does not yet exist. Writes with if_version=new to an existing path are rejected so you can't overwrite content you haven't seen. Both the rejection and a version conflict return the current content (when it is within the read cap) so you can merge and retry; an oversized document's content is withheld and must be replaced wholesale. The result includes the new version token for follow-up writes. Never write secrets or credentials into a memory — project stores are shared with every collaborator, and such writes are refused in every store.
