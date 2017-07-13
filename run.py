#!flask/bin/python
from app import app
import os.environ
port = int(os.environ.get('PORT', 5000))
debug = False if os.environ.get('ENVIRONMENT') == 'production' else True
app.run(port=port, debug=debug)