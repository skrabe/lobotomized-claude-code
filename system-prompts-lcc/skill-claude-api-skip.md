<!--
name: claude-api skill SKIP guidance
description: >-
  The SKIP guidance for the claude-api skill (other providers), injected into
  model context alongside the trigger.
ccVersion: 2.1.206
-->
SKIP only when another provider is being worked on (overrides all triggers): OpenAI/GPT/Gemini/Llama/Mistral/Cohere/Ollama named in the query; OR `grep -rE 'openai|langchain_openai|google.generativeai|genai|mistralai|cohere|ollama'` over the project hits (run this grep FIRST if no provider named — don't Read the file).
