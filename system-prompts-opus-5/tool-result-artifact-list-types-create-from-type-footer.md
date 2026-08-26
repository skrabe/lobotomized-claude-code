<!--
name: 'Tool Result: Artifact List Types Create-From-Type Footer'
description: >-
  list_types footer explaining how to start a new Artifact from a type when
  type-create is on.
ccVersion: 2.1.246
-->
To start a new Artifact from one, publish with its `type_url` and no files first — the result carries the type's instructions for its data files — then publish the data files to the returned `url`. `action: "describe_type"` with a `type_url` shows a type's files first if you need them.
