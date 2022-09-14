#!/usr/bin/env python
from setuptools import setup, find_packages, Distribution
import codecs
import os.path

# Make sure versiontag exists before going any further
Distribution().fetch_build_eggs("versiontag>=1.2.0")

from versiontag import get_version, cache_git_tag  # NOQA


packages = find_packages("src")

install_requires = [
    "Django>=3.2",
    "requests>=2.9.1",
    "djangorestframework>=3.11",
    "python-dateutil>=2.5.2",
]

extras_require = {
    "development": [
        "coverage>=4.4.2",
        "flake8>=3.5.0",
        "responses>=0.5.1",
        "tox>=2.9.1",
        "versiontag>=1.2.0",
    ],
}


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return codecs.open(fpath(fname), encoding="utf-8").read()


cache_git_tag()

setup(
    name="django-ups-tnt",
    description="Django wrapper around UPS Time In Transit JSON API",
    version=get_version(pypi=True),
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    author="David Burke",
    author_email="dburke@thelabnyc.com",
    url="https://gitlab.com/thelabnyc/django-ups-tnt",
    license="ISC",
    package_dir={"": "src"},
    packages=packages,
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extras_require,
)
