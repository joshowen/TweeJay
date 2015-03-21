import soco

from tweejay.music import get_spotify_track_uri


if __name__ == "__main__":
    sonos = soco.discover().pop()

#     spotify_plugin = Spotify(sonos)
    track_uri = get_spotify_track_uri("Notorious Juicy")
#     track_uri = 'spotify:track:3dbCYM0LJR8tiL0W1XXmpK'
#
#     track = SpotifyTrack(track_uri)
#
#
#     spotify_plugin.add_track_to_queue(track)

    from soco.plugins.spotify import Spotify
    from soco.plugins.spotify import SpotifyTrack
    # create a new plugin, pass the soco instance to it
    myplugin = Spotify(sonos)
    print 'index: ' + str(myplugin.add_track_to_queue(SpotifyTrack(track_uri)))
#     print 'index: ' + str(myplugin.add_album_to_queue(SpotifyAlbum('spotify:album:6a50SaJpvdWDp13t0wUcPU')))
