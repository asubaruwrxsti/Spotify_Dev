from flask import current_app
from flask.views import MethodView
import requests

class GetSpotifyCode(MethodView):
    def get(self):
        url = "https://accounts.spotify.com/authorize"
        params = {
            "client_id": current_app.config["SPOTIFY"]["client_id"],
            "response_type": "code",
            "redirect_uri": current_app.config["SPOTIFY"]["redirect_uri"],
            "scope": current_app.config["SPOTIFY"]["scope"]
        }

        return (requests.get(url, params=params)).text