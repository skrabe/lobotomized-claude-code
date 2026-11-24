<!--
name: 'System Reminder: Unsupported connector file reference refusal'
description: >-
  Tells Claude nothing was sent because this connector tool can't take a
  sha256:<hash>:<path> file reference and takes a file only in the form its
  description gives
ccVersion: 2.1.331
-->
Nothing was sent: this tool can't be given a file by reference, and it would have got the file's path and hash as text, not the file. It takes a file only in the form its description gives. Any whole value of the form sha256:<hash>:<path> is stopped here, even one not meant as a reference.
