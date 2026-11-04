<!--
name: 'Tool Result: MCP resource outside loaded skills'
description: >-
  ReadMcpResource error telling the model a resource was not read because no
  loaded skill from that server lists the address, and how to build a listed
  address.
ccVersion: 2.1.318
-->
This resource was not read, because no skill that is loaded from this server lists this address. While a skill from this server is loaded, this tool reads from this server only the files that a loaded skill lists. For a file of a loaded skill, copy the address after "at" in that skill's first sentence, character for character, without the full stop. Then add "/" and the file's path. If this conversation does not hold that sentence, load that skill here: its first sentence then gives the address. To read a file of another skill of this server, load that skill first.
