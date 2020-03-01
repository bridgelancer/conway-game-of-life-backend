# A Flask-SocketIO server for the Multiplayer Conway's Game of Life

[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) is a well known zero-player cellular automaton that is capable of generate complex pattern with some initial state. The general rules of this multiplayer version of the game is as follows:


1. Each player is assigned a random colour
2. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
3. Any live cell with two or three live neighbors lives on to the next generation.
4. Any live cell with more than three live neighbors dies, as if by overcrowding.
5. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
6. When a dead cell revives by rule #4 “Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.”, it will be given a color that is the average of its neighbors (that revive it).

This server now initiates a `50*100` orthgonal, finite board for grid placing.


In this repository, a multiplayer version of such game is enabled by a Flask-SocketIO server. Any frontend client would need to open a connection to the backend via a [socket.io-client](https://socket.io/docs/client-api/). An SocketIO connection should be opened to `https://server_domain/test`.

Upon connection to the server, a `confirm connect` SocketIO event would be returned to the corresponding connection. Any board update would be pushed to the client via a `boardUpdated` event. 

For a client to push updates from client, a `boardUpdate` event should be sent to the server with the opened socket.

An example of such implemented client could be found on the associated repository [here](https://github.com/bridgelancer/conway-game-of-life-frontend).

## Quick start
Python 3.6+ is requried for development of the project.

Source code of this project could be found on this [Github link](https://github.com/bridgelancer/conway-game-of-life-backend). To clone the repository to the current working directory, run

`git clone https://github.com/bridgelancer/conway-game-of-life-backend.git`

A running instance of the server is also deployed on [Heroku](https://conway-game-of-life-backend.herokuapp.com/).

To initialize the project, please run the following commands in sequence first:

Virtual environment configuration
1. `export PYTHONPATH=src/to/comway/backend/`
2. `python3 -m venv venv`
3. `. venv/bin/activate`
4. `pip install -r requirements.py`

The above commands creates the virtual environment that contains the appropriate versions of dependencies according to the requirements file.

To start the server, activate the Python virtual environment and run:
`python app.py`

A eventlet server would be fired up if dependencies are installed properly, listening to `http://127.0.0.1:5000`.

## Testing
[Pytest](https://docs.pytest.org/en/latest/index.html) is used. To run the test batteries, execute `pytest` after virtual environment is launched.

## Deploy to Heroku
Various strategies could be used to deploy this codebase onto your own Heroku account including using the HerokuCLI and Github continous-delivery approaches.

Installation guide of HerokuCLI on various systems could be found on their [Dev Center Site](https://devcenter.heroku.com/articles/heroku-cli).

After [logging in](https://devcenter.heroku.com/articles/authentication) to your Heroku account via HerokuCLI, create a new Heroku app for this project on your account by running

`heroku create`

### Environment variable setup
As per documentation, environmental variables of a Heroku dyne instance could be set via HerokuCLI or via the web application.

In the git repository, run 
`heroku config:set PYTHONPATH=/app`
to set up the absolute imports paths.

### Manual deploy by HerokuCLI
A remote of `heroku` would be setup to this newly created Heroku project for deployment. To deploy, simply push a master branch to the heroku remote with
`git push heroku master`

### Github continous integration and delivery
Travis-CI continous delivery and continous integration for Github are also being setup within this repository to ensure each pull request made to master would be tested against the test batteries.

Heroku could pull code from Github whenever the master branch of the repository is pushed after receiving OAuth authorization and proper configuration. This could be set up in the `Deploy` tab of the Heroku Dashboard app. The detailed documentation could be found [here](https://devcenter.heroku.com/articles/github-integration). In this repository, the code base would be deployed to heroku after the build process of Travis-CI passed.


## Design choices
Python Socket-IO server is leveraged for the backend, wrapping an underlying Flask application. Socket-IO client library handles multiple transport protocols (most notably WebSocket andHTML long polling) that does not restrain the client side choices. The underlying [eventlet](https://eventlet.net/) network library handles concurrent websockets connections in reasonable performance for the functioning of the prototype. This is in contrary to the usual `node` server in this repository. This is because the author has more experience in the associated python tool chain for the prioritization of development speed. 


## Tradeoffs and Todos
In the current deployment strategy, a gunicorn web server is used that does not support multiple workers due to its load balancing strategy. An nginx web server might be preferred in case more connections need to be served. In such a case, additional infrastructure has to built for horizontal sclaing and handling of messages across workers.

Due to time limitation constraint, a naive approapch is used to update board color, with whole board being recalculated for each received updates from clients. A more efficient approach is to only receive any changes made on the client side, update those cells correspondingly and send back the differences to the client after backend computation.
