<!--
name: 'Skill: Artifact Capabilities Verify Declared Endpoints'
description: >-
  Fragment of the artifact-capabilities skill prompt telling the model to call
  get_endpoints once and call_endpoint on each GET route before handing over the
  link.
ccVersion: 2.1.280
-->
for declared endpoints, `get_endpoints` once and one `call_endpoint` on each GET route (a writing route only when the user wants a test record made)
