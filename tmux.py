'''Destyny of this file is comunicate with tmux'''

import subprocess


def get_variable_from_conf(var_name):
    bit, _ = subprocess.Popen(
        f'tmux show-options -gv @{var_name}', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True
    ).communicate()
    return bit.decode('utf-8').replace('\n', '')


MAX_LEN_STATUS = int(get_variable_from_conf('spotify_max_len_status'))
RE_STATUS = get_variable_from_conf('spotify_re_status')
