<!--
name: 'Plugin marketplace add: supported git URL forms'
description: >-
  List of supported git address forms (https, http, ssh, user@host:path,
  host-less file://; git:// refused as unencrypted), interpolated after
  'Supported:' in the invalid-git-URL errors.
ccVersion: 2.1.285
-->
https, http, ssh (also written git+ssh or ssh+git), user@host:path, or a local file:// address with no host. git:// isn't supported because it isn't encrypted.
