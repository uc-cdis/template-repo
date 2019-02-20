#!/usr/bin/env bash

echo -e '\e[1mYour cookie is cut successfully, running post-cut operations now.\e[0m'

echo -e '\e[1mLocking dependencies...\e[0m'
{% if cookiecutter.package_type == 'Library' %}
rm -rf ./deployment ./openapi ./Dockerfile ./dockerrun.bash ./build_openapi.py run.py
{% endif %}
pipenv lock -r > requirements.txt
pipenv --rm

echo -e '\e[1mCreating git repository...\e[0m'
git init
git add -A .
git commit -m 'Cut from gh:uc-cdis/template-repo'
git remote add origin git@github.com:uc-cdis/{{ cookiecutter.package_name }}.git

echo -e '\e[1mYour new {{ cookiecutter.package_type.lower() }} is ready under: \e[31m{{ cookiecutter.package_name }}\e[0m'
