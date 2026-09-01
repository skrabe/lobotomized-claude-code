<!--
name: 'Tool Description: ReadFile'
description: Tool description for reading files
ccVersion: 2.1.128
variables:
  - MAX_LINES_CONSTANT
  - CONDITIONAL_LENGTH_NOTE
  - CAT_DASH_N_NOTE
  - READ_FULL_FILE_NOTE
  - CAN_READ_PDF_FILES_FN
  - ADDITIONAL_READ_NOTE
-->
Reads a file from the local filesystem. Assume it can read any file on the machine; assume a user-provided path is valid. Reading a nonexistent file is fine — an error is returned.

Usage:
- file_path must be an absolute path, not relative
- Reads up to ${MAX_LINES_CONSTANT} lines from the start by default${CONDITIONAL_LENGTH_NOTE}
${CAT_DASH_N_NOTE}
${READ_FULL_FILE_NOTE}
- Reads images (PNG, JPG, etc.) — contents are presented visually.${CAN_READ_PDF_FILES_FN()?`
- Reads PDFs (.pdf). For PDFs over 10 pages, provide the pages parameter to read specific ranges (e.g. pages: "1-5"); reading a large PDF without it will fail. Max 20 pages per request.`:""}
- Reads Jupyter notebooks (.ipynb) — returns all cells with their outputs
- Files only, not directories — list a directory with the shell tool
- For a screenshot path the user provides, use this tool to view it (works with temporary file paths)
- An existing but empty file returns a system-reminder warning in place of contents${ADDITIONAL_READ_NOTE}
