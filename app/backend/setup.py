import os
import re

import pkg_resources
from pkg_resources import parse_requirements
from setuptools import find_packages, setup

app_name = 'example_backend'
base_path = os.path.dirname(__file__)

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

packages = find_packages()


def get_reqs(lines):
    return [str(r) for r in parse_requirements(lines)]


def get_requirements(req_path, exclude=[]):
    reqs = []
    dir_name = os.path.dirname(req_path)
    with open(req_path) as requirements:
        pattern = re.compile("-r (.+)")
        for line in requirements.readlines():
            match = pattern.match(line)
            if match:
                dep_reqs = os.path.join(dir_name, match.group(1))
                with open(dep_reqs) as dep_requirements:
                    for dep_line in dep_requirements.readlines():
                        reqs.append(dep_line.rstrip())
                reqs += get_requirements(dep_reqs, exclude=exclude)
                continue
            package = line.rstrip()
            if package not in exclude:
                reqs.append(package)
    return reqs


exclude_packages = []
reqs = get_requirements(os.path.join(base_path, 'requirements.txt'), exclude=exclude_packages)


def get_package_name(req_name):
    discr = pkg_resources.get_distribution(req_name)
    top_level = open(discr._provider.egg_info + '/top_level.txt')
    return top_level.readlines()[0].rstrip(), discr.location


version = '1.0.0'

setup_cnf = {
    'name': app_name,
    'version': version,
    'python_requires': '>=3.7',
    'packages': find_packages(exclude=('venv',)),
    'include_package_data': True,
    'entry_points': {
        'console_scripts': [
            'run_app=example_backend.main:run_app',
        ],
    },
}
setup(**setup_cnf, install_requires=reqs)
