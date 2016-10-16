"""Sphinx configuration file."""

import os
import sys
import time


# General configuration.
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
author = '@Robpol86'
copyright = '{}, {}'.format(time.strftime('%Y'), author)
master_doc = 'index'
project = __import__('setup').NAME
pygments_style = 'friendly'
release = version = __import__('setup').VERSION
templates_path = ['_templates']
extensions = list()


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
html_title = project


# autodoc
extensions.append('sphinx.ext.autodoc')


# extlinks.
extensions.append('sphinx.ext.extlinks')
extlinks = {'github': ('https://github.com/robpol86/{0}/blob/v{1}/%s'.format(project, version), '')}


# google analytics
extensions.append('sphinxcontrib.googleanalytics')
googleanalytics_id = 'UA-82627369-1'


# SCVersioning.
scv_banner_greatest_tag = True
scv_grm_exclude = ('.gitignore', '.nojekyll', 'README.rst')
scv_show_banner = True
scv_sort = ('semver', 'time')
