import requests
class Spotify:
    def __init__(self, client_id, client_secret, user_id, redirect_uri, scope="user-read-private user-read-email"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_id = user_id
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.token = self.fetchToken()
    
    def fetchToken(self):
        # Example from Spotify API:
        #curl -X POST "https://accounts.spotify.com/api/token" \
        # -H "Content-Type: application/x-www-form-urlencoded" \
        # -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"

        url = "https://accounts.spotify.com/api/token"

        # Fetch token from the API
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(url, data=data)
        return response.json()["access_token"]

    def getCode(self):
        # Example from Spotify API:
        # https://accounts.spotify.com/authorize?client_id=5fe01282e44241328a84e7c5cc169165&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-read-private%20user-read-email&state=34fFs29kd09

        url = "https://accounts.spotify.com/authorize"
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "scope": self.scope
        }
        response = requests.get(url, params=params)
        return response.json()

    def fetchPlaylist(self, user, playlist_id):
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
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def fetchPlaylistTracks(self, playlist_id, limit=10, offset=0):
        # Example from Spotify API:
        # GET https://api.spotify.com/v1/playlists/{playlist_id}/tracks

        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

        # Fetch the tracks
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers, params={"limit": limit, "offset": offset})
        return response.json()

    def fetchMySavedTracks(self, limit=10, offset=0):
        # Example from Spotify API:
        # GET https://api.spotify.com/v1/me/tracks

        url = f"https://api.spotify.com/v1/me/tracks"

        # Fetch the tracks
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers, params={"limit": limit, "offset": offset, "grant_type": "authorization_code", "code": self.token})
        return response.json()