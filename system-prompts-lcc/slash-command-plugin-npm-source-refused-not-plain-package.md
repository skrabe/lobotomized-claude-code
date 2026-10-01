<!--
name: 'Slash Command: Plugin npm Source Refused (Not A Plain Package)'
description: >-
  Plugin install refusal when an npm plugin source is neither a registry package
  name nor a tarball link, pointing git plugins to github, url or git-subdir
  sources
ccVersion: 2.1.286
variables:
  - SLASH_COMMAND_PLUGIN_NPM_SOURCE_REFUSED_NOT_PLAIN_PACKAGE_VAR_0
-->
it ${SLASH_COMMAND_PLUGIN_NPM_SOURCE_REFUSED_NOT_PLAIN_PACKAGE_VAR_0}. An npm plugin source must name a registry package (name or name@version) or link to a tarball file. For a plugin in a git repository, use a "github", "url" or "git-subdir" source.
