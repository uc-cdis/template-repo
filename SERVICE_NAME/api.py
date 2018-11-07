import flask
import logging
import time

from SERVICE_NAME import auth
from SERVICE_NAME.errors import AuthZError
from SERVICE_NAME.admin import blueprint as admin_bp
from .errors import JWTError

app = flask.Flask(__name__)


@app.route('/user_endpoint', methods=['GET'])
def do_something_connected():
    """
    User endpoint
    """
    token = flask.request.headers.get('Authorization')
    try:
        user = auth.current_user # raises error if user is not connected
        return 'Success! User is {}'.format(user.username), 200
    except JWTError as e:
        return e.message, e.code


@app.route('/_status', methods=['GET'])
def health_check():
    """
    Health check endpoint
    ---
    tags:
      - system
    responses:
      200:
        description: Healthy
      default:
        description: Unhealthy
    """
    return 'Healthy', 200


def app_init(app):
    app.logger.info('Initializing app')
    start = time.time()

    # do the necessary here!

    app.logger.info('Registering blueprints')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    end = int(round(time.time() - start))
    app.logger.info('Initialization complete in {} sec'.format(end))


def run_for_development(**kwargs):
    app.logger.setLevel(logging.INFO)

    # load configuration
    app.config.from_object('SERVICE_NAME.dev_settings')

    try:
        app_init(app)
    except:
        app.logger.exception("Couldn't initialize application, continuing anyway")
    app.run(**kwargs)