from {{ cookiecutter.package_name }}.api import run_for_development


if __name__ == '__main__':

    run_for_development(debug=True, threaded=True)
