<!--
name: 'Tool Description: Upload Image'
description: >-
  Description of the upload_image browser tool: upload a captured/uploaded image
  to a file input or drag-and-drop target via ref or coordinate.
ccVersion: 2.1.268
-->
Upload a screenshot you took with the computer tool's screenshot action to a file input or drag & drop target. Screenshot IDs expire a few minutes after capture, so take the screenshot of what you want to upload right before uploading. Don't reuse an ID that an upload already failed with: to retry, take a new screenshot of the same content, and retry that upload at most once (never after the user declined). This tool cannot upload user-attached images or other files; use file_upload with the file's path for those, if that tool is available. Two approaches: (1) ref — for specific elements, especially hidden file inputs; (2) coordinate — for drag & drop to visible locations like Google Docs. Provide either ref or coordinate, not both.
