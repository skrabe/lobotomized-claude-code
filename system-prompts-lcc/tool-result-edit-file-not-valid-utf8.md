<!--
name: 'Tool Result: Edit file not valid UTF-8'
description: >-
  Validation error returned when an edit targets a file that is not valid UTF-8;
  tells the model to use a shell command or ask the user before converting.
ccVersion: 2.1.296
-->
File is not valid UTF-8. It may use a legacy encoding such as Windows-1252, Shift-JIS or GBK, or be binary. This tool saves the whole file as UTF-8, which would replace every byte it cannot decode with U+FFFD. Nothing was written. Make the change with a shell command that reads and writes the file in its own encoding, or ask the user whether to convert the file to UTF-8 first.
