'''This is heart of the plugin'''

from spotify import ALBUM, ARTIST, SONG, PLAYBACKSTATUS
from tmux import MAX_LEN_STATUS, RE_STATUS


def create_status():
    new_status = RE_STATUS
    for re, data in [
            ('#{spotify_album}', ALBUM), ('#{spotify_artist}', ARTIST), ('#{spotify_song}', SONG),
            ('#{spotify_playback}', PLAYBACKSTATUS)
    ]:
        new_status = new_status.replace(re, data)
    return make_short_status(new_status)


def make_short_status(new_status):
    return new_status[:MAX_LEN_STATUS - 5] + '(...)' if len(new_status) > MAX_LEN_STATUS else new_status


if __name__ == 'main':
    print(create_status())
