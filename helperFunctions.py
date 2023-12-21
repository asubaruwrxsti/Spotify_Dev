import requests

def loadEnv(default=".env"):
    # Load environment variables as a dictionary
    env = {}
    with open(f"{default}", "r") as f:
        for line in f:
            if line[0] != '#':
                key, value = line.strip().split('=')
                env[key] = value
    return env

def fetchToken(client, secret):
    # Example from Spotify API:
    #curl -X POST "https://accounts.spotify.com/api/token" \
    # -H "Content-Type: application/x-www-form-urlencoded" \
    # -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"

    url = "https://accounts.spotify.com/api/token"

    # Fetch token from the API
    data = {
        "grant_type": "client_credentials",
        "client_id": client,
        "client_secret": secret
    }
    response = requests.post(url, data=data)
    return response.json()["access_token"]

def getCode(client, redirect_uri, scope="user-read-private user-read-email"):
    # Example from Spotify API:
    # https://accounts.spotify.com/authorize?client_id=5fe01282e44241328a84e7c5cc169165&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-read-private%20user-read-email&state=34fFs29kd09

    url = "https://accounts.spotify.com/authorize"
    params = {
        "client_id": client,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": scope
    }
    response = requests.get(url, params=params)
    return response.json()

def fetchPlaylist(token, user, playlist_id):
    # Example from Spotify API:
    # GET https://api.spotify.com/v1/playlists/{playlist_id}

    if playlist_id == "":
        # Get the user's playlists
        url = f"https://api.spotify.com/v1/users/{user}/playlists"
    else:
        # Get the playlist
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    
    # Fetch the playlist
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def fetchPlaylistTracks(token, playlist_id, limit=10, offset=0):
    # Example from Spotify API:
    # GET https://api.spotify.com/v1/playlists/{playlist_id}/tracks

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    # Fetch the tracks
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, params={"limit": limit, "offset": offset})
    return response.json()

def fetchMySavedTracks(token, limit=10, offset=0):
    # Example from Spotify API:
    # GET https://api.spotify.com/v1/me/tracks

    url = f"https://api.spotify.com/v1/me/tracks"

    # Fetch the tracks
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers, params={"limit": limit, "offset": offset, "grant_type": "authorization_code", "code": token})
    return response.json()