<!--
name: 'Tool Result: Git Bundle Git Dir Tampered'
description: >-
  Refuses the upload when the git directory changed mid-build, holds something
  git never puts there, or could not be inspected.
ccVersion: 2.1.246
-->
Not uploading this working tree: its git directory changed while the upload was being prepared, holds something git itself never puts there, or could not be inspected — another git process (a background fetch or gc) may have written packs meanwhile, in which case let it finish and retry; otherwise look for a commondir or objects/info/alternates file, or a link, special or unreadable entry where its branches, tags, HEAD, the temporary refs/seed entries, their logs, or objects go (commondir, refs/heads, refs/tags, refs/seed, logs/refs/seed, logs/HEAD, objects/info, objects/pack) before retrying.
