<!--
name: Artifact files Source HTML/SVG/XML Not Copyable
description: >-
  files-map error forbidding server-side copy of an HTML or XML document from
  another Artifact, telling Claude to read it with read_file and publish its own
  file.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_ARTIFACT_FILES_SOURCE_HTML_SVG_XML_NOT_COPYABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_FILES_SOURCE_HTML_SVG_XML_NOT_COPYABLE_VAR_1
-->
files: the source for ${TOOL_RESULT_ARTIFACT_FILES_SOURCE_HTML_SVG_XML_NOT_COPYABLE_VAR_0(TOOL_RESULT_ARTIFACT_FILES_SOURCE_HTML_SVG_XML_NOT_COPYABLE_VAR_1)} would copy an HTML or XML document from another Artifact, which is never allowed — read it with action "read_file" and publish it as your own file
