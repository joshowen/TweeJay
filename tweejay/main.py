from tweejay import music


if __name__ == "__main__":
    print music.get_spotify_track_uri('greenday dookie')
    print music.get_spotify_track_uri('green day dookie')
    print music.get_spotify_track_uri('taylor swift')
#     sp = spotipy.Spotify()
#
#     results = sp.search(q='Notorious Juicy', limit=20)
#     track = next((r for r in results['tracks']['items'] if r['explicit']), None)
#     if not track:
#         # Go with the lame non-explicit version
#         track = next(results['tracks']['items'], None)
#     if track:
#         print track['name']
#         print track['uri']
#     return
