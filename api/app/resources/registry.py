from flask import jsonify
from api.app.resources.user.blueprint import register_user_bp
from api.app.resources.blog.blueprint import register_blog_bp


def register_resource(app_):
    @app_.route('/ping', methods=['GET'])
    def hello_world():
        return jsonify({'message': 'PONG'})

    register_user_bp(app_)
    register_blog_bp(app_)
    register_demo_bp(app_)


from flask import Flask, Blueprint
from flask.views import MethodView

demo_bp = Blueprint("demo", __name__, url_prefix="/demo")


def register_demo_bp(app_: Flask):
    demo_bp.add_url_rule("/hello1", view_func=hello_world)
    demo_bp.add_url_rule('/hello2', 'hello2', HelloWorldView.as_view('hello2'))

    app_.register_blueprint(demo_bp)


def hello_world():
    return jsonify({'message': 'Hello, World!'})


class HelloWorldView(MethodView):
    def get(self):
        return jsonify({'message': 'Hello, World!'})

    def post(self):
        return jsonify({'message': 'This is a POST request'})
