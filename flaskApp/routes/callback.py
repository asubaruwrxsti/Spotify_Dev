from flask import render_template
from flask.views import MethodView

class Callback(MethodView):
    def get(self):
        return render_template('index.html')