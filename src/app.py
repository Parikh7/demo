import os
import signal
import subprocess
import sys
import threading
import time

import ffmpeg
import openai
import tiktoken
import torch
import whisper
from flask import Flask, render_template
from controllers.main_controller import main_controller
from dotenv import load_dotenv

app = Flask(__name__)

# Register the main_controller blueprint
app.register_blueprint(main_controller)

if __name__ == "__main__":
    app.run(debug=True)


