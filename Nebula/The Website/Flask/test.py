from flask import Flask, request, render_template,jsonify
import os
import sys

api_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../The AI/v0/API'))
if api_path not in sys.path:
    sys.path.insert(0, api_path)

from chatbot import LocalAIChatbot

model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../The AI/v0/Models/llama2.gguf'))
if not os.path.isfile(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

chatbot = LocalAIChatbot(model_path=model_path)

answer = chatbot.chat("hi im Ethan, how are you?")
print(answer)