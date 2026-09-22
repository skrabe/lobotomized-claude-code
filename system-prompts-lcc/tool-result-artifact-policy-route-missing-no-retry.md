<!--
name: Artifact Policy Route Missing No Retry
description: >-
  Suffix of the artifact org-policy error that tells the model a 404 will
  persist, not to retry, and to tell the user their IT admin must allow the
  address.
ccVersion: 2.1.280
-->
, and a proxy or gateway that does not forward that path will keep answering 404, so nothing in this session can load it. Do not retry this call. Tell the user that their IT admin needs to let that address through to the API.
