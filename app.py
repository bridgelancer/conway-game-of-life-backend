"""Flask-SocketIO server for handling websockets transmission"""
import threading
import json

from flask import Flask, render_template, current_app
from flask_socketio import SocketIO, emit

from backend.engine.conway import convert_current_grid

# Standard setup for Flask with SocketIO wrapping
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# cors_allowed_origins options used for simplicity in testing
socketio = SocketIO(app, cors_allowed_origins='*')

# Initialize current board on server side
ROWS = 50
COLUMNS = 100
INIT_CELL = {'color': 'white', 'fixed': False}
current_board = [[INIT_CELL for c in range(COLUMNS)] for r in range(ROWS)]

thread = None

def comway_thread(app):
    global current_board
    i = 0
    with app.app_context():
        while True:
            test_str = f'{i*1} seconds elapsed'
            current_board = convert_current_grid(current_board)
            # socketio.emit('my response', {'data': test_str}, namespace='/test')
            socketio.emit('tick', json.dumps({'data': current_board}), namespace='/test')
            socketio.sleep(5)
            i += 1


@socketio.on('connect', namespace='/test')
def test_connect():
    print('One client connected...')

    emit('confirm connect', {})
    emit('boardUpdated', json.dumps({'data': (current_board)}))
    print('Board initiation broadcasted')

    global thread
    if thread is None:
        print('starting one thread...')
        app = current_app._get_current_object()
        thread = socketio.start_background_task(target=comway_thread, app=app)

@socketio.on('boardUpdate', namespace='/test')
def broadcast_update(event):
    global current_board
    board = json.loads(event)['data']
    current_board = board
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
