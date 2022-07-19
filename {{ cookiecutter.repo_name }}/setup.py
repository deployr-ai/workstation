from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    version='0.0.1'
)
