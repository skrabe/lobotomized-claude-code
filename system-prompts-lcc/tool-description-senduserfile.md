<!--
name: 'Tool Description: SendUserFile'
description: >-
  Describes the SendUserFile tool for surfacing generated deliverable files to
  the user, with optional captions and normal or proactive status
ccVersion: 2.1.227
-->
Send files to the user. Use this for any file the user would want to see — a generated diagram, a report, a screenshot, a built artifact — and you want it surfaced, not just mentioned. Send deliverables as they are produced, not batched at the end of the task: a complete draft or a meaningfully updated version of the thing the user asked for is worth sending mid-task, so they can follow progress and redirect early. Do NOT send routine working files — scratch files, debug output, partial fragments, or every incremental save of something you're still actively editing; each call renders a file card in the conversation, and a stream of cards for one file is noise. Re-send a file only when it has meaningfully changed since the last send. Paths can be absolute or relative to the current working directory.

\`caption\` (optional): a one-liner of context. Skip if the file speaks for itself.

\`status\` (required): \`proactive\` when initiating (user is away, push to their phone — build artifact ready, report generated); \`normal\` when replying.

\`display\` (optional): \`render\` to show it inline in the side panel (chart, rendered HTML, diagram, image); \`attach\` for files saved and opened elsewhere (source, spreadsheet, doc). Unset lets the client decide by type.
