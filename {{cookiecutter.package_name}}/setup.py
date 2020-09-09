"""
This is a file to describe the Python module distribution and
helps with installation.

More info on various arguments here:
https://setuptools.readthedocs.io/en/latest/setuptools.html
"""
from setuptools import setup, find_packages
{%- if cookiecutter.package_type == 'Library' %}
from subprocess import check_output


def get_version():
    # https://github.com/uc-cdis/dictionaryutils/pull/37#discussion_r257898408
    try:
        tag = check_output(
            ["git", "describe", "--tags", "--abbrev=0", "--match=[0-9]*"]
        )
        return tag.decode('utf-8').strip("\n")
    except Exception:
        raise RuntimeError(
            "The version number cannot be extracted from git tag in this source "
            "distribution; please either download the source from PyPI, or check out "
            "from GitHub and make sure that the git CLI is available."
        )
{%- endif %}


setup(
    name="{{ cookiecutter.package_name }}",
{%- if cookiecutter.package_type == 'Library' %}
    version=get_version(),
{%- endif %}
    description="{{ cookiecutter.package_type }} Template",
    url="https://github.com/occ-data/{{ cookiecutter.package_name }}",
    license="Apache",
    packages=find_packages(),
{%- if cookiecutter.package_type == 'Library' %}
    install_requires=[
        "cdiserrors~=0.1",
    ],
{%- endif %}
)
