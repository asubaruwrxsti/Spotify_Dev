import helperFunctions as hf
env = hf.loadEnv()

if __name__ == "__main__":
    # Setup
    client = env["CLIENT"]
    secret = env["SECRET"]
    user = env["MY_USER_ID"]

    # Fetch token
    token = hf.fetchToken(client, secret)
    print(f"Token: {token} \n\n")

    # Fetch playlists
    playlists = hf.fetchPlaylist(token, user, "")
    for playlist in playlists["items"]:
        print(f"{playlist['name']} - {playlist['id']}")
    
    print("\n\n")

    # Fetch tracks
    playlist_id = playlists["items"][0]["id"]
    try:
        playlist_items = hf.fetchPlaylistTracks(token, playlist_id, 1)
        for track in playlist_items["items"]:
            print(f"{track['track']['name']} - {track['track']['id']}")
    except:
        print(playlist_items)
    
    print("\n\n")

    # Fetch my saved tracks, needs code to work
    #tracks = hf.fetchMySavedTracks(token)
    #try:
    #    for track in tracks["items"]:
    #        print(f"{track['track']['name']} - {track['track']['id']}")
    #except:
    #    print(tracks)