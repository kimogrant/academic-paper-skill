#!/usr/bin/env bash
# Install PaperCraft (academic-paper-skill) into .cursor/skills/academic-paper-skill/
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="academic-paper-skill"

usage() {
  cat <<EOF
Usage:
  ./skill.sh list
  ./skill.sh install /path/to/target/project

Installs: SKILL.md, references/, examples/, scripts/, VERSION
  -> <target>/.cursor/skills/${SKILL_NAME}/

Invoke in Cursor: /academic-paper-skill (display name: PaperCraft)
EOF
}

copy_skill() {
  local dest="$1"
  mkdir -p "${dest}"
  cp "${ROOT}/SKILL.md" "${ROOT}/VERSION" "${dest}/"
  rm -rf "${dest}/references" "${dest}/examples" "${dest}/scripts"
  cp -R "${ROOT}/references" "${dest}/references"
  cp -R "${ROOT}/examples" "${dest}/examples"
  if [[ -d "${ROOT}/scripts" ]]; then
    cp -R "${ROOT}/scripts" "${dest}/scripts"
  fi
}

cmd="${1:-}"
case "$cmd" in
  list)
    echo "academic-paper-skill / PaperCraft (v$(tr -d '\r\n' < "${ROOT}/VERSION"))"
    echo "  ${ROOT}/SKILL.md"
    echo "  references/: $(find "${ROOT}/references" -name '*.md' | wc -l | tr -d ' ') files"
    ;;
  install)
    target="${2:-}"
    if [[ -z "$target" ]]; then
      usage
      exit 1
    fi
    abs_target="$(cd "$target" && pwd)"
    dest="${abs_target}/.cursor/skills/${SKILL_NAME}"
    copy_skill "${dest}"
    echo "Installed to ${dest}"
    echo "Reload Cursor, then invoke: /academic-paper-skill"
    ;;
  *)
    usage
    exit 1
    ;;
esac
