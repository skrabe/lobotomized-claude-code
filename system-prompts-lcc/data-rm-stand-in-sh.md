<!--
name: 'Data: rm stand-in script'
description: >-
  Shell stand-in for rm in hosted sessions whose refusal message reaches the
  model through Bash output.
ccVersion: 2.1.330
-->
#!/bin/sh
# Stand-in for rm, first on PATH in hosted sessions while its flag is served (src/utils/shell/rmGuard.ts).
# Apart from shell builtins, the only program it runs is the next rm on PATH. It records fixed codes only, never a path or command text.
set +euxv  # bash run as sh turns these on from an exported SHELLOPTS: -e would let a failed write stop rm, and -x and -v would print paths.
words=__RM_GUARD_WORDS__
outcome=__RM_GUARD_OUTCOME__
refuse=__RM_GUARD_REFUSE__
own=__RM_GUARD_OWN__
many=20

is_system_folder() {
  case "$1" in
    /|/bin|/boot|/dev|/etc|/lib|/lib32|/lib64|/libx32|/nix|/nix/store|/opt|/proc|/run|/sbin|/srv|/sys|/usr|/var|/var/lib) return 0;;
    /usr/bin|/usr/sbin|/usr/lib|/usr/lib32|/usr/lib64|/usr/libexec|/usr/lib/x86_64-linux-gnu|/usr/lib/aarch64-linux-gnu) return 0;;
    /usr/local|/usr/share|/usr/include|/usr/lib64/ld-linux-x86-64.so.2|/usr/lib/ld-linux-aarch64.so.1) return 0;;
  esac
  return 1
}

# Prints a rank from 0 (nothing to note) to 5 (the root); the case below names each. The worst operand decides.
# A many_ rank means at least $many operands in a row directly inside that folder. This moves to each folder to resolve links, so it runs in a subshell.
worst_rank() {
  worst=0
  note() { [ "$1" -le "$worst" ] || worst=$1; }
  options_over=0
  last_dir=
  last_real=
  run_parent=
  run=0
  here=
  if cd -P . 2>/dev/null; then here=$PWD; fi
  for a in "$@"; do
    if [ "$options_over" = 0 ]; then
      case "$a" in --) options_over=1; continue;; -?*) continue;; esac
    fi
    case "$a" in
      '') continue;;
      /*) p=$a;;
      *) [ -n "$here" ] || continue; p=$here/$a;;
    esac
    # bash keeps a leading // through cd and pwd, and it would match no name below.
    while :; do case "$p" in //*) p=\${p#/};; *) break;; esac; done
    slash=0
    while :; do case "$p" in /) break;; */) slash=1; p=\${p%/};; *) break;; esac; done
    base=\${p##*/}
    dir=\${p%/*}
    [ -n "$dir" ] || dir=/
    # rm refuses a path ending in . or .., so such an operand removes nothing.
    case "$base" in .|..) continue;; esac
    # With a trailing slash rm follows a link, so the whole path is resolved, last part included.
    if [ "$slash" = 1 ] || [ -z "$base" ]; then dir=$p; base=; fi
    if [ "$dir" != "$last_dir" ]; then
      last_dir=$dir
      if cd -P -- "$dir" 2>/dev/null; then last_real=$PWD; else last_real=$dir; fi
      while :; do case "$last_real" in //*) last_real=\${last_real#/};; *) break;; esac; done
    fi
    if [ -n "$base" ]; then
      full=\${last_real%/}/$base
      parent=$last_real
    else
      full=$last_real
      parent=\${full%/*}
      [ -n "$parent" ] || parent=/
    fi
    case "$full" in
      /) note 5;;
      /home|/root) note 3;;
      *) if is_system_folder "$full"; then note 3; fi;;
    esac
    # This script's own folder, what is in it, and the folders above it: without this script, a loop's next rm would go unchecked.
    case "$full" in "$own"|"$own"/*) note 2;; esac
    case "$own" in "$full"/*) note 2;; esac
    if [ "$parent" = "$run_parent" ]; then run=$((run + 1)); else run_parent=$parent; run=1; fi
    if [ "$run" -ge "$many" ] && is_system_folder "$parent"; then
      if [ "$parent" = / ]; then note 4; else note 1; fi
    fi
  done
  echo "$worst"
}

# Search from after this file's last PATH entry: an rm wrapper listed before that entry would call this script again.
# The entries ahead of this file come last, for an rm that only they hold.
run_next_rm() {
  # Match this file by its path text first: -ef touches every entry's rm on disk, so a dead mount listed after the rm that will run could hang this script.
  # -ef stays for a call by a path that no entry spells.
  for same in = -ef; do
    left=$PATH:
    walked=
    after=$left
    before=
    found=
    while [ -n "$left" ]; do
      d=\${left%%:*}
      left=\${left#*:}
      if [ "\${d:-.}/rm" "$same" "$0" ]; then after=$left; before=$walked; found=1; else walked=$walked$d:; fi
    done
    [ -z "$found" ] || break
  done

  # exec by name, so that rm's own messages still begin "rm:", with PATH cut so that the name finds this rm.
  # The rm found may be another session's stand-in, which then does the same.
  left=$after$before
  kept=
  while [ -n "$left" ]; do
    d=\${left%%:*}
    left=\${left#*:}
    if [ -x "\${d:-.}/rm" ] && [ ! -d "\${d:-.}/rm" ]; then
      PATH=$kept$d\${left:+:\${left%:}}
      exec rm "$@"
    fi
    kept=$kept$d:
  done
  printf '%s\\n' 'rm: command not found' >&2
  exit 127
}

# The subshell keeps every cd away from where rm runs. Where it can't start, at a session's task limit, the shell exits with 2, or 254 under bash, and rm runs unchecked.
# bash also comes here on a fatal signal, with $? at 0, and then rm must not run.
trap 'case $? in 2|254) trap - EXIT; run_next_rm "$@";; esac' EXIT
rank=$(worst_rank "$@") 2>/dev/null
check_status=$?
trap - EXIT
# A signal that ended only the subshell leaves $rank empty. In refuse mode that must not pass as a safe rm, so rm does not run; in log mode rm runs anyway.
if [ "$refuse" = 1 ] && [ "$check_status" -gt 128 ]; then
  printf '%s\\n' "This rm did not run, and nothing was removed: a signal stopped its safety check." >&2
  exit "$check_status"
fi

case "$rank" in
  5) reason=root why='the root folder';;
  4) reason=many_root_entries why='many items directly inside the root folder';;
  3) reason=system_folder why='a system folder or file';;
  2) reason=own_folder why="Claude Code's rm check, or a folder that holds it";;
  1) reason=many_system_folder_entries why='many items directly inside a system folder';;
  *) reason=;;
esac

# Written before anything is removed: this rm may delete the words file, and the shell with it. Past a file-size limit the write would kill this shell.
trap '' XFSZ
{
  if [ -f "$words" ]; then
    [ -s "$words" ] || printf 'first_rm_seen\\n' >>"$words"
    [ -z "$reason" ] || printf '%s_%s\\n' "$outcome" "$reason" >>"$words"
  fi
} 2>/dev/null
trap - XFSZ

if [ -n "$reason" ] && [ "$refuse" = 1 ]; then
  printf '%s\\n' "This rm did not run, and nothing was removed: it named $why. Don't delete that another way: tell the user what you were trying to do. To delete your own files, give paths inside your work folder." >&2
  exit 1
fi

run_next_rm "$@"
