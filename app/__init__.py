from flask import Flask, jsonify
import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        return jsonify(message="Welcome to Pepsales!!!")
    
    @app.route("/env")
    def env():
        print(os.environ.get("TEST_SECRET"))
        return jsonify(message=os.environ.get("TEST_SECRET","Key not found"))

    return app