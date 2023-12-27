from flask import render_template, current_app
from flask.views import MethodView

class Index(MethodView):
    def get(self):
        message = "No spotify code provided"

        if current_app.config["SPOTIFY"]["code"] != None:
            message = "Authorized with Spotify, code: " + current_app.config["SPOTIFY"]["code"]

        tracks = current_app.config["SPOTIFY"]["object"].fetchMySavedTracks()
        return render_template('index.html', message=message, tracks=tracks)