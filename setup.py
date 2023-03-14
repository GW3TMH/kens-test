#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

authors_name = 'Ken Williams'
authors_email = 'ken@kensmail.uk'
github_url = 'https://github.com/GW3TMH/kens-test'
package_name = 'kens-test'
short_description = 'Demonstrates TKinter snap'

def get_version():
    import ast
    
    filename = package_name +'/__init__.py'
    
    try:
        with open(filename) as input_file:
            for line in input_file:
                if line.startswith('__version__'):
                    input_file.close()
                    return ast.parse(line).body[0].value.s
    except IOError:
        return '1.0'


def get_long_description():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except IOError:
        return 'Long Description'


def get_requirements():
    try:
        with open('requirements.txt', 'r') as f:
            return f.read().splitlines()
    except IOError:
        return "['None']"


setup(
    name=package_name,
    version=get_version(),
    install_requires=get_requirements(),
    author=authors_name,
    author_email=authors_email,
    description=short_description,
    url=github_url,
    long_description=get_long_description(),
    packages=[package_name, 'bin'],
    include_package_data=True,
    entry_points = "{'console_scripts': ['" +package_name + " = bin." +package_name +":main']}",
    license='License :: OSI Approved :: MIT License',
)
