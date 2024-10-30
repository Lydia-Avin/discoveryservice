from flask import Flask, jsonify
import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        return jsonify(message="Welcome to Pepsales!")
    
    @app.route("/env")
    def env():
        return jsonify(message=os.getenv("TEST_SECRET","Key not found"))
    
    @app.route("/health")
    def health():
        return jsonify(message="health check OK")

    return app