<!--
name: 'Tool Parameter: Artifact lang'
description: >-
  zod .describe() for the Artifact tool's lang input, telling the model to pass
  the BCP-47 tag of the page's text content on every publish
ccVersion: 2.1.246
-->
BCP-47 language tag of the page's text content ("ja", "pt-BR") — becomes the page's <html lang>. Match the content's language, not the conversation's; for mixed content use the dominant language. Pass on every publish.
