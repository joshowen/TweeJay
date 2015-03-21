import soco
from soco.plugins.spotify import Spotify, SpotifyTrack
from tweejay.music import get_spotify_track_uri

sonos = soco.discover().pop()

spotify_plugin = Spotify(sonos)
track_uri = get_spotify_track_uri("Notorious Juicy")

track = SpotifyTrack(track_uri)

spotify_plugin.add_track_to_queue(track)

