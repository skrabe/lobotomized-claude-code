<!--
name: 'Tool result: git bundle ambiguous filter driver'
description: >-
  Refusal when git configuration defines a filter driver named "unset" or
  "unspecified", so files would upload unfiltered.
ccVersion: 2.1.291
-->
Not uploading this working tree: your git configuration defines a filter driver named "unset" or "unspecified" (a file your configuration includes counts too, even one included only for other repositories), and git reports files that use such a driver as having no filter, so they would be uploaded as they are on disk, without the filter. Nothing was uploaded. Rename the driver in your git configuration, and in any attributes file that uses it, then retry.
