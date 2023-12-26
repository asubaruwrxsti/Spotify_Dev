from flask.views import MethodView
from flask import render_template, current_app

class GetSpotifyCode(MethodView):
    def get(self):
        params = {
            "client_id": current_app.config["SPOTIFY"]["client_id"],
            "response_type": "code",
            "redirect_uri": current_app.config["SPOTIFY"]["redirect_uri"],
            "scope": current_app.config["SPOTIFY"]["scope"]
        }

        return render_template('getSpotifyCode.html', params=params)