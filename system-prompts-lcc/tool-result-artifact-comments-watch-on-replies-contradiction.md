<!--
name: 'Tool Result: ArtifactComments Watch On/Replies Contradiction'
description: >-
  validateInput contradiction when watch sets on:false and replies:true
  together; returned as {result:false,message} and becomes the tool_result.
ccVersion: 2.1.257
-->
watch: `on: false` stops the watch and `replies: true` resumes automatic replies on it — pass one, not both
