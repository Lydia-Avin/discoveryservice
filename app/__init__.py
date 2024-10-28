from flask import Flask, jsonify
import os

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        return jsonify(message="Welcome to Pepsales!!!")
    
    @app.route("/env")
    def env():
        return jsonify(message=os.environ.get("AWS_ACCESS_KEY_ID"))

    return app