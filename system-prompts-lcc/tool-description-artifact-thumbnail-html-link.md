<!--
name: 'Tool Description: Artifact thumbnail HTML link'
description: >-
  Artifact-tool description fragment explaining how a rel=artifact-thumbnail
  link tag sets the gallery/link-preview image.
ccVersion: 2.1.251
-->
`<link rel="artifact-thumbnail" href="thumb.png">` at the top of the HTML (the same first 8KB as the title) sets the artifact's gallery and link-preview image: a PNG or JPEG of about 1200×630 and at most 1MB, saved next to the HTML file and referenced by a relative path. A second such tag with `media="(prefers-color-scheme: dark)"` sets a dark-mode variant. Without the tag, a screenshot of the page is used.
