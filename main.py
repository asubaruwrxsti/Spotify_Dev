import helperFunctions as hf
import spotifyClient.spotifyClient as spotifyClient
import flaskApp.flaskLib as flaskLib

env = hf.loadEnv()

if __name__ == "__main__":
    # Setup environment variables
    client = env["CLIENT"]
    secret = env["SECRET"]
    user = env["MY_USER_ID"]

    # Create a Flask object
    flask = flaskLib.FlaskLib()
    flask.run()

    # Create a Spotify object
    # spotify = spotifyClient.Spotify(client, secret , user , "http://localhost:8080/callback", "user-read-private user-read-email")