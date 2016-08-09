import os
import sys

from setuptools import find_packages, setup

PROJECT_DIR = os.path.dirname(__file__)

sys.path.append(os.path.join(PROJECT_DIR, 'src'))
from svg_icons import get_version  # noqa isort:skip


setup(
    name='django-svg-icons',
    version=get_version().replace(' ', '-'),
    author="Mike Dingjan",
    author_email='mike@mikedingjan.nl',
    url='https://github.com/mikedingjan/django-svg-icons',
    description='Django SVG Icons made easy',
    long_description=open(os.path.join(PROJECT_DIR, 'README.md')).read(),
    keywords='SVG icons, django icons',
    platforms=['osx', 'linux'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='Apache License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
