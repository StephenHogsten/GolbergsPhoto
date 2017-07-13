#!flask/bin/python
from app import app
from os import environ
port = int(environ.get('PORT', 5000))
debug = False if environ.get('ENVIRONMENT') == 'production' else True
app.run(port=port, debug=debug)