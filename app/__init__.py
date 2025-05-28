from flask import Flask

app = Flask(__name__)

from app import chat, libros, tareas, youtube, realtime, hola_mundo, hola_flask

