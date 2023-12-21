import flask
from .routes.index import Index

class FlaskLib:
    def __init__(self, port=8080):
        self.app = flask.Flask(__name__, template_folder="views")
        self.port = port
        self.routes = {}

        # Add default routes
        self.addRoute("/", Index, "index")

    def run(self):
        self.app.run(port=self.port)
    
    def addRoute(self, route, route_class, view, methods=["GET"]):
        self.app.add_url_rule(route, view_func=route_class.as_view(view), methods=methods)
        self.routes[route] = route_class