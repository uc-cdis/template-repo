from cdiserrors import *
{% if cookiecutter.package_type == 'Service' %}
from authutils.errors import JWTError
{% endif %}


class CustomException(APIError):
    def __init__(self, message):
        self.message = str(message)
        self.code = 500
