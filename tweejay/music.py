import spotipy


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
