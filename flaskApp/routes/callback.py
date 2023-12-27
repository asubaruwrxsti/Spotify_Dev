from flask import render_template, current_app
from flask.views import MethodView
from flask import request

class Callback(MethodView):
    def get(self):
        # Read the spotify code from the url
        code = request.args.get('code')

        # Save the code to the flask app
        current_app.config["SPOTIFY"]["code"] = code
        return render_template('callback.html', code=code)