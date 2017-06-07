#!/usr/bin/env python3

from setuptools import setup

setup(
    name='polyproject',
    version='1.0',
    description='Python package to project a point onto a polyhedron',
    author='Praveen Venkatesh',
    url='https://github.com/praveenv253/polyproject',
    packages=['polyproject', ],
    install_requires=['numpy', 'scipy', 'cvxpy', ],
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', ],
    license='MIT',
)
