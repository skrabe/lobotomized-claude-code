<!--
name: 'Tool Result: Artifact List Types Create-From-Type Footer'
description: >-
  list_types footer explaining how to start a new Artifact from a type when
  type-create is on.
ccVersion: 2.1.269
-->
To start a new Artifact from one, publish with its \`type_url\`, a \`title\` (what the user called it, or a short descriptive name) and no files first (passing \`auto_open: "after_first_write"\` when you will fill it next) — the result carries the new Artifact's \`url\` and the type's instructions, and says how to fill it: documents written to its own store, or data files published to that \`url\`.${TOOL_RESULT_ARTIFACT_LIST_TYPES_CREATE_FROM_TYPE_FOOTER_VAR_0()?` ${TOOL_RESULT_ARTIFACT_LIST_TYPES_CREATE_FROM_TYPE_FOOTER_VAR_1}`:""} ${TOOL_RESULT_ARTIFACT_LIST_TYPES_CREATE_FROM_TYPE_FOOTER_VAR_2} with a \`type_url\` shows a type's files first if you need them.${TOOL_RESULT_ARTIFACT_LIST_TYPES_CREATE_FROM_TYPE_FOOTER_VAR_3("",()=>" For a slide deck or a visual design, list the design systems this user can open (`action: \"list\"` with that type's name as `type`) before choosing any typeface or palette, unless the user named or declined one: use the one marked default without asking — it is the user's standing choice, however brief the request; if some are listed but none is default, name them and ask; if none, choose your own look.")}
