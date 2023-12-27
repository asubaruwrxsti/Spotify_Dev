import helperFunctions as hf
import spotifyClient.spotifyClient as spotifyClient
import flaskApp.flaskApp as flaskApp

env = hf.loadEnv()

if __name__ == "__main__":
    # Create a Flask object
    flask = flaskApp.FlaskApp()
    flask.run()