#!/usr/bin/env bash

plugin_path="$(tmux show-env -g TMUX_PLUGIN_MANAGER_PATH | cut -f2 -d=)"

update_tmux_option() {
    local option="$1"
    local string="$(tmux show-option -gqv "$option")"
    local value="$(python3 ${plugin_path}tmux-spotify/plug.py)"
    local interpolation="\#{spotify_status_b}"
    local string=${string/$interpolation/$value}
    tmux set-option -gq "$option" "$string"
    echo "$string"
}

main() {
    update_tmux_option "status-right"
    update_tmux_option "status-left"
}
main
