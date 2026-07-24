#!/usr/bin/env bash
set -euo pipefail

disabled_sources=()

restore_sources() {
  local status=$?
  trap - EXIT INT TERM

  for backup in "${disabled_sources[@]}"; do
    original="${backup%.sbmi-disabled}"
    if sudo test -e "$backup"; then
      sudo mv "$backup" "$original"
      echo "restored_apt_source=$original"
    fi
  done

  exit "$status"
}

trap restore_sources EXIT INT TERM

while IFS= read -r source; do
  [[ -n "$source" ]] || continue
  backup="${source}.sbmi-disabled"

  if sudo test -e "$backup"; then
    echo "stale_disabled_source=$backup" >&2
    echo "Restaure ou remova o arquivo de backup antes de continuar." >&2
    exit 1
  fi

  sudo mv "$source" "$backup"
  disabled_sources+=("$backup")
  echo "temporarily_disabled_apt_source=$source"
done < <(
  grep -l "dl\.yarnpkg\.com" \
    /etc/apt/sources.list.d/*.list \
    /etc/apt/sources.list.d/*.sources \
    2>/dev/null || true
)

python -m playwright install --with-deps chromium
