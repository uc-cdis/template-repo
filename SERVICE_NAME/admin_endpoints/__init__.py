from flask import Blueprint

from SERVICE_NAME import auth
from SERVICE_NAME.errors import JWTError


blueprint = Blueprint('admin', __name__)


@blueprint.route('')
def do_something_important():
    """
    Admin endpoint
    """
    try:
        auth.current_user.require_admin() # raises error if user is not admin
        return 'Success! User is admin', 200
    except JWTError as e:
        return e.message, e.code


@blueprint.route('/is_admin')
def check_if_user_is_admin():
    """
    Admin endpoint
    """
    # check if user is admin (raises error if user is not connected)
    if auth.current_user.is_admin:
        return 'Success! User is admin', 200
    else:
        return 'Woops! User is not admin', 403