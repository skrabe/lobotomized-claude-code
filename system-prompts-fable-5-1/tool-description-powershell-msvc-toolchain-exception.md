<!--
name: PowerShell tool description — MSVC toolchain exception
description: >-
  Windows-only fragment of the PowerShell Bash tool description noting the MSVC
  toolchain is only on PATH inside a Visual Studio developer shell.
ccVersion: 2.1.199
-->

   - Exception: the MSVC toolchain (`cl`, `nmake`, `msbuild`) is only on PATH inside a Visual Studio developer shell, so it may be installed even if not listed. Environment changes do NOT persist between commands, so initialize and build in ONE command: `cmd /c '"C:\Program Files\Microsoft Visual Studio\<year>\<edition>\VC\Auxiliary\Build\vcvarsall.bat" x64 && <build command>'`
