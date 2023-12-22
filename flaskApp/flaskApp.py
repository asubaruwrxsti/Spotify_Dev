import flask
from .routes.index import Index
from .routes.callback import Callback
import helperFunctions as hf
import spotifyClient.spotifyClient as spotifyClient
from .routes.getSpotifyCode import GetSpotifyCode

class FlaskApp:
    # Load .env file
    env = hf.loadEnv()

    def __init__(self, port=8080):
        self.app = flask.Flask(
            __name__, 
            template_folder="views"

        )
        self.port = port
        self.routes = {}
        
        # Add Spotify configuration to app config
        self.app.config['SPOTIFY'] = {
            "client_id": self.env["CLIENT"],
            "client_secret": self.env["SECRET"],
            "redirect_uri": self.env["REDIRECT_URI"],
            "scope": self.env["SCOPE"],
            "user_id": self.env["MY_USER_ID"],
            "object": None,
            "code": None
        }

        # Add default routes
        self.addRoute("/", Index, "index")
        self.addRoute("/callback", Callback , "callback")
        self.addRoute("/getSpotifyCode", GetSpotifyCode, "getSpotifyCode")
        
        # Create a Spotify object
        self.app.config['SPOTIFY']['object'] = spotifyClient.Spotify(self.env["CLIENT"], self.env["SECRET"], self.env["MY_USER_ID"], "http://localhost:8080/callback", "user-read-private user-read-email")

    def run(self):
        self.app.run(port=self.port)
    
    def addRoute(self, route, route_class, view, methods=["GET"]):
        self.app.add_url_rule(route, view_func=route_class.as_view(view), methods=methods)
        self.routes[route] = route_class