from flask import Blueprint, request


blueprint = Blueprint('something', __name__)


@blueprint.route('', methods=['GET'])
def get_something():
    """
    Get something
    """
    return 'I got something'


@blueprint.route('', methods=['PUT'])
def put_something():
    """
    Put something
    """
    return 'I put something'


@blueprint.route('/put-get', methods=['GET', 'PUT'])
def get_put_something():
    """
    Several methods for the same function
    """
    if request.method == 'GET':
        return 'I got something, did not put'
    else:
        return 'I put something, did not get'


@blueprint.route('/bar', methods=['GET'])
@blueprint.route('/foo/<param>', methods=['GET'])
def do_something(param=None):
    """
    Several routes for the same function
    """
    return 'I did something with {}'.format(request.url_rule)