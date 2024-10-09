from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        return jsonify(message="Welcome to Pepsales! Testing:(!")

    return app
