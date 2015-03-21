import soco
from soco.plugins.spotify import Spotify, SpotifyTrack

def add_song_to_queue(track_uri):
  myplugin = Spotify(get_sonos())
  track = SpotifyTrack(track_uri)
  myplugin.add_track_to_queue(track)
  return track

def get_currently_playing():
  return get_sonos().get_current_track_info()

def get_sonos():
  return list(soco.discover())[-1]

    