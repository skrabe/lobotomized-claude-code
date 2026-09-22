<!--
name: 'Tool Result: Git Bundle Shallow Second Name'
description: >-
  Remedy clause when a cloud bundle upload refuses because the shallow file has
  a second name.
ccVersion: 2.1.280
-->
 Git never gives it a second name. Look at it (ls -l) and remove the other name if you can find it (`find . -samefile` with the file named above, run in this directory); or copy the file named above to a new name and move the copy over it. Then retry.
