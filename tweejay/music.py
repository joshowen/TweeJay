import os
import spotipy
import soundcloud
import pprint

def get_spotify_track_uri(query):
    sp = spotipy.Spotify()

    results = (r for r in sp.search(q=query, limit=50)['tracks']['items'] if 'US' in r['available_markets'])
    track = next((r for r in results if r['explicit']), None)

    if not track:
        # Go with the lame non-explicit version
        track = next(results, None)
    if track:
        return track['uri']
    return None


def get_soundcloud_track_uri(query):
  sc = soundcloud.Client(client_id=os.environ.get('SOUNDCLOUD_CLIENT_ID'))
  tracks = sc.get('/tracks', q=query, license='cc-by-sa')
  stream_url = sc.get(tracks[0].stream_url, allow_redirects=False)
  return stream_url.location
