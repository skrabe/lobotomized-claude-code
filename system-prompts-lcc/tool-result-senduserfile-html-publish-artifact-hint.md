<!--
name: 'Tool Result: SendUserFile HTML publish-as-artifact hint'
description: >-
  Hint after sending an HTML file that it can also be published as an artifact,
  with the cases where not to.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_SENDUSERFILE_HTML_PUBLISH_ARTIFACT_HINT_VAR_0
  - TOOL_RESULT_SENDUSERFILE_HTML_PUBLISH_ARTIFACT_HINT_VAR_1
  - TOOL_RESULT_SENDUSERFILE_HTML_PUBLISH_ARTIFACT_HINT_VAR_2
-->
If an HTML file you just sent is a page for people to read, you can also publish it as an artifact: give its path to ${TOOL_RESULT_SENDUSERFILE_HTML_PUBLISH_ARTIFACT_HINT_VAR_0(TOOL_RESULT_SENDUSERFILE_HTML_PUBLISH_ARTIFACT_HINT_VAR_1,TOOL_RESULT_SENDUSERFILE_HTML_PUBLISH_ARTIFACT_HINT_VAR_2)}, as a new version if it came from an artifact you published. Don't if the user asked for the HTML itself ("give me the html"; asking for an HTML page isn't that), or if the user presented it as sensitive, or if it imitates a real organization, person or record.
