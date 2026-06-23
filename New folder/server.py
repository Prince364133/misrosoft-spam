from flask import Flask, jsonify
from flask_cors import CORS
import keyboard

app = Flask(__name__)

CORS(app)

@app.route("/keys")
def keys():

    pressed = []

    def on_key(event):

        pressed.append(event.name)

        print("Pressed:", event.name)

    keyboard.on_press(on_key)

    return jsonify({
        "status": "Keyboard listener started"
    })

app.run(port=5000) 