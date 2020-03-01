# Backend server for the Multiplayer Conway Game of Life

Description of the problem and the solution

How to test/build/deploy/use your solution. LInk to the hosted application if
applicable (heroku/netlify)

Reasoning behind your technical choices, including architectural

Trade-offs you might have made, anything you left out, or what you might do
differently if you were to spend additional time on the project.

## Quick start
To initialize the project, please run the following commands first:

1. `export PYTHONPATH='src/to/comway/'`
2. `python3 -m venv venv`
3. `. venv/bin/activate`
4. `pip install -r requirements.py`

To start the server, execute
1. `python app.py`

A eventlet server would be fired up if dependencies are installed properly.

## Design choices

## Testing
[Pytest](https://docs.pytest.org/en/latest/index.html) is used. To run tthe test batteries, execute `pytest` after virtual environment is launched.
