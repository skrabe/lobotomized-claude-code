<!--
name: 'Tool Result: Artifact Publish Host Grant Readback Page Remedy'
description: >-
  Page-lane remedy appended when host-grant-bounded capability readback keeps
  failing: declare capabilities and contract latest.
ccVersion: 2.1.273
-->
 If the read keeps failing, publish the page declaring the capabilities you intend (capabilities: {} clears the stored declaration) together with contract: 'latest', which needs no read.
