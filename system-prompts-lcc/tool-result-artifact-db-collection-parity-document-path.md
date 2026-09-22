<!--
name: Artifact Db Collection Parity Document Path
description: >-
  write_db/read_db validation error when collection has even segments and is
  therefore a document path.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_DB_COLLECTION_PARITY_DOCUMENT_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_COLLECTION_PARITY_DOCUMENT_PATH_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_COLLECTION_PARITY_DOCUMENT_PATH_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_COLLECTION_PARITY_DOCUMENT_PATH_VAR_3
  - TOOL_RESULT_ARTIFACT_DB_COLLECTION_PARITY_DOCUMENT_PATH_VAR_4
-->
collection '${TOOL_RESULT_ARTIFACT_DB_COLLECTION_PARITY_DOCUMENT_PATH_VAR_0(TOOL_RESULT_ARTIFACT_DB_COLLECTION_PARITY_DOCUMENT_PATH_VAR_1)}' has ${TOOL_RESULT_ARTIFACT_DB_COLLECTION_PARITY_DOCUMENT_PATH_VAR_2} segments, which makes it a document path, not a collection: collection paths have an odd number of segments (collection/document/collection/…) and the document is collection + doc_id. For that document use collection '${TOOL_RESULT_ARTIFACT_DB_COLLECTION_PARITY_DOCUMENT_PATH_VAR_3}' with doc_id '${TOOL_RESULT_ARTIFACT_DB_COLLECTION_PARITY_DOCUMENT_PATH_VAR_4}'; for a collection inside it, add one more segment. Per-user data follows the same rule — collection 'data/users/<id>' (3 segments) holds that user's documents, so 'data/users/<id>/decks' is one document and 'data/users/<id>/decks/cards' a collection.
