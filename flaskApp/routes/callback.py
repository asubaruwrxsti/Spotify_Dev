from flask import render_template
from flask.views import MethodView
from flask import request

class Callback(MethodView):
    def get(self):
        # Read the spotify code from the url
        code = request.args.get('code')
        return render_template('callback.html', code=code)