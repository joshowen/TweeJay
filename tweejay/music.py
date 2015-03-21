import spotipy


def get_spotify_track_uri(query):
    sp = spotipy.Spotify()

    results = sp.search(q=query, limit=50)
    track = next((r for r in results['tracks']['items'] if r['explicit']), None)
    if not track:
        # Go with the lame non-explicit version
        track = next(iter(results['tracks']['items']), None)
    if track:
        return track['uri']
    return None

