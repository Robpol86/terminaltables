"""Sphinx configuration file."""

import os
import time
from subprocess import check_output

import sphinx_rtd_theme

SETUP = os.path.join(os.path.dirname(__file__), '..', 'setup.py')


# General configuration.
author = check_output([SETUP, '--author']).strip().decode('ascii')
copyright = '{}, {}'.format(time.strftime('%Y'), author)
master_doc = 'index'
nitpicky = True
project = check_output([SETUP, '--name']).strip().decode('ascii')
release = version = check_output([SETUP, '--version']).strip().decode('ascii')


# Options for HTML output.
html_context = dict(
    conf_py_path='/docs/',
    display_github=True,
    github_repo=os.environ.get('TRAVIS_REPO_SLUG', '/' + project).split('/', 1)[1],
    github_user=os.environ.get('TRAVIS_REPO_SLUG', 'robpol86/').split('/', 1)[0],
    github_version=os.environ.get('TRAVIS_BRANCH', 'master'),
    source_suffix='.rst',
)
html_copy_source = False
html_favicon = 'favicon.ico'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_title = project


# Extensions.
extensions = ['sphinx.ext.extlinks']
extlinks = {'github': ('https://github.com/robpol86/{0}/blob/v{1}/%s'.format(project, version), '')}
