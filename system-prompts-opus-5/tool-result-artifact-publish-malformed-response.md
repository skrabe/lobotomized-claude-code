<!--
name: Artifact publish returned a malformed response
description: >-
  Publish failure reason returned to the model when the deploy server's response
  is incomplete or malformed. CC 2.1.239 hoisted the leading ${VAR_0} out of the
  template into a literal argument of the dto() builder, so the same prompt now
  arrives as a call-site literal; id reused from 2.1.238.
ccVersion: 2.1.239
-->
deploy returned an incomplete or malformed response
