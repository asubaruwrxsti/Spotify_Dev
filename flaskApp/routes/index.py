from flask import render_template, current_app
from flask.views import MethodView
import spotifyClient.spotifyClient as spotifyClient

class Index(MethodView):
    def get(self):
        message = "Unauthorized with Spotify."
        if current_app.config["SPOTIFY"]["code"] != None:
            message = "Authorized with Spotify, code: " + current_app.config["SPOTIFY"]["code"]
        return render_template('index.html', message=message)