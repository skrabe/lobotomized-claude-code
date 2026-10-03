<!--
name: 'Data: strictKnownMarketplaces.(settings).name setting description'
description: >-
  Description of the `strictKnownMarketplaces.(settings).name` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.288
-->
Marketplace name, as stored in known_marketplaces.json. A reserved name is refused per entry at load (revalidateReservedNameEntry); a look-alike name is judged when that marketplace's own catalog is parsed (catalogNameSchemaFor).
