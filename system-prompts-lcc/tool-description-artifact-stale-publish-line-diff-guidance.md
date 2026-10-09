<!--
name: 'Tool Description: Artifact stale publish line diff guidance'
description: >-
  Refuses stale Artifact publishes with a live-page line diff, marks the live
  version viewed, and requires merging its changes into the file being published
ccVersion: 2.1.295
variables:
  - STALE_VERSION_REFUSAL_LEAD
  - LIVE_ARTIFACT_READ_RESULT
  - FORMAT_NUMBER_FN
  - LINE_DIFF_RESULT
  - PLURALIZE_FN
  - UNCOMPARED_CONTENT_NOTE
  - SAVED_SOURCE_LOCATION_NOTE
  - SAVED_SOURCE_SHAPE_DESCRIPTION_FN
  - UNTRUSTED_DIFF_AND_SAVED_FILE_NOTE
  - FORCE_REFUSAL_NOTE
  - LINE_DIFF_READING_LEGEND
  - LIVE_VERSION_DIFF_HEADER_FN
  - ARTIFACT_SLUG
  - AUTHORED_BY_OTHERS_MARKER
-->
${STALE_VERSION_REFUSAL_LEAD} Against the content you just sent, the live page (version ${LIVE_ARTIFACT_READ_RESULT.ver}) differs in ${FORMAT_NUMBER_FN(LINE_DIFF_RESULT.hunks)} ${PLURALIZE_FN(LINE_DIFF_RESULT.hunks,"place")}: ${FORMAT_NUMBER_FN(LINE_DIFF_RESULT.liveOnly)} ${PLURALIZE_FN(LINE_DIFF_RESULT.liveOnly,"line")} on the live page that yours lacks and ${FORMAT_NUMBER_FN(LINE_DIFF_RESULT.sentOnly)} only in yours, shown in full below as a line diff, so that version now counts as viewed${UNCOMPARED_CONTENT_NOTE}.
${SAVED_SOURCE_LOCATION_NOTE}; that file is ${SAVED_SOURCE_SHAPE_DESCRIPTION_FN(!0)}. Merge by carrying the live page's lines into YOUR file — or copy the saved file and apply your edits to the copy, leaving the saved file itself as it is — and publish that file with file_path; do not resend your previous content unchanged, do not copy the diff marks into the page, and do not rebuild from memory.${UNTRUSTED_DIFF_AND_SAVED_FILE_NOTE}${FORCE_REFUSAL_NOTE} ${LINE_DIFF_READING_LEGEND}
${LIVE_VERSION_DIFF_HEADER_FN(ARTIFACT_SLUG)}${AUTHORED_BY_OTHERS_MARKER}
