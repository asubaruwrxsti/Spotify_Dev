import requests

class Spotify:
    def __init__(self, client_id, client_secret, user_id, redirect_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_id = user_id
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.token = self.fetchToken()
        self.code = ""
    
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
            "client_secret": self.client_secret,
            "scope": self.scope,
        }
        response = requests.post(url, data=data)
        return response.json()["access_token"]

    def fetchPlaylist(self, user, playlist_id = None):
        # Example from Spotify API:
        # GET https://api.spotify.com/v1/playlists/{playlist_id}

        if playlist_id == None:
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

        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers, params={"limit": limit, "offset": offset})
        return response.json()