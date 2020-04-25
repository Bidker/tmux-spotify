#!/usr/bin/env bash

plugin_path="$(tmux show-env -g TMUX_PLUGIN_MANAGER_PATH | cut -f2 -d=)"

interpolation="\#{spotify_status}"

update_tmux_option() {
    local value=run-shell "python3 ${CURRENT_DIR}/plug.py"
    local string=${$interpolation/$value}
    local option="$1"
    tmux set-option -gq "$option" "$string"
}

main() {
    update_tmux_option "status-right"
    update_tmux_option "status-left"
}
main
