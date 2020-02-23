import json

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Standard setup for Flask with SocketIO wrapping
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# cors_allowed_origins options used for simplicity in testing
socketio = SocketIO(app, cors_allowed_origins='*')

ROWS = 50
COLUMNS = 100

INIT_CELL = {'color': 'white', 'fixed': False, 'selected': False}
currentBoard = [[INIT_CELL for c in range(COLUMNS)] for r in range(ROWS)]

@socketio.on('connect', namespace='/test')
def test_connect():
    print('One client connected...')

    emit('confirm connect', {})
    emit('boardUpdated', json.dumps({'data': (currentBoard)}))

@socketio.on('boardUpdate', namespace='/test')
def broadcast_update(event):
    global currentBoard
    currentBoard= json.loads(event)['data']
    emit('boardUpdated', event, broadcast=True, include_self=False)
    print('Board update broadcasted')

@socketio.on('my event', namespace='/test')
def test_message(event):
    print(f'Message recived from client: {event["data"]}')
    emit('my response', {'data': event['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_broadcast_message(event):
    print(f'Broadcast message recived from client: {event["data"]}')
    emit('my response', {'data': event['data']}, broadcast=True)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
