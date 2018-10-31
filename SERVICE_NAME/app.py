import flask

app = flask.Flask(__name__)

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