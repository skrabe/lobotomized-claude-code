<!--
name: 'Data: Built-in gh stand-in title/text file guidance'
description: >-
  gh stand-in help rule: write each title or text to a new file outside the
  checkout with a file tool, pass it with -F (not -f), never on the command
  line, and end a title without a newline
ccVersion: 2.1.331
-->
Write each title or text to a new file outside the checkout with a file tool, not the shell, and pass it with a capital -F (-f sends the literal @path). Never put it on the command line. The file is sent as it is: end a title without a newline.
