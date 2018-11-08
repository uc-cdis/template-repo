from service_name.api import app

# wsgi.ini references this file

config = app.config

config['API_URL'] = 'http://peregrine-service/v0/submission/graphql/'
application = app
