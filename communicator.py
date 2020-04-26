'Destyny of this file is comunicate with spotify-cli-linux (https://github.com/pwittchen/spotify-cli-linux) and tmux'

import subprocess


def exec_in_sys(command):
    bit, _ = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True
    ).communicate()
    return bit.decode('utf-8').replace('\n', '')


def get_var_from_spotify(element):
    return exec_in_sys('spotifycli --%s' % element)


def get_var_from_tmux(var_name):
    return exec_in_sys('tmux show-options -gv @%s' % var_name)


ALBUM = get_var_from_spotify('album')
SONG = get_var_from_spotify('song')
ARTIST = get_var_from_spotify('artist')
PLAYBACKSTATUS = get_var_from_spotify('playbackstatus') + ' '

MAX_LEN_STATUS = int(get_var_from_tmux('spotify_max_len_status'))
RE_STATUS = get_var_from_tmux('spotify_re_status')
