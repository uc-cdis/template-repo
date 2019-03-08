assert (
    "{{ cookiecutter.package_name }}".isalnum()
    and "{{ cookiecutter.package_name }}".islower()
    and "{{ cookiecutter.package_name }}"[0].isalpha()
), "{{ cookiecutter.package_name }} is not a valid name, please use only [a-z][a-z0-9]*"
