from flask import Flask, render_template, request
import threading
import game

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    game_thread = threading.Thread(target=game.run_game)
    game_thread.start()
    return "O jogo de digitação foi iniciado! Verifique a janela do Pygame."

if __name__ == '__main__':
    app.run(debug=True)
