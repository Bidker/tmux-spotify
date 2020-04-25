'''Destyny of this file is comunicate with spotify-cli-linux (https://github.com/pwittchen/spotify-cli-linux)'''

import subprocess


def get_from_spotify(element):
    bit, _ = subprocess.Popen(
        'spotifycli --%s' % element, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True
    ).communicate()
    return bit.decode('utf-8').replace('\n', '')


ALBUM = get_from_spotify('album')
SONG = get_from_spotify('song')
ARTIST = get_from_spotify('artist')
PLAYBACKSTATUS = get_from_spotify('playbackstatus') + ' '
