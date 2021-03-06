"""Sphinx configuration file."""

import os
import sys
import time


# General configuration.
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
author = '@Robpol86'
copyright = '{}, {}'.format(time.strftime('%Y'), author)
html_last_updated_fmt = '%c {}'.format(time.tzname[time.localtime().tm_isdst])
master_doc = 'index'
project = 'InfluxDB Home Monitoring'
pygments_style = 'friendly'
templates_path = ['_templates']
extensions = list()


# Options for HTML output.
html_context = dict(
    conf_py_path='/docs/',
    display_github=True,
    github_repo=os.environ.get('CIRCLE_PROJECT_REPONAME', 'influxdb'),
    github_user=os.environ.get('CIRCLE_PROJECT_USERNAME', 'robpol86'),
    github_version=os.environ.get('TRAVIS_BRANCH', 'master'),
    source_suffix='.rst',
)
html_copy_source = False
html_favicon = 'favicon.ico'
html_theme = 'sphinx_rtd_theme'
html_title = project


# autosectionlabel
extensions.append('sphinx.ext.autosectionlabel')


# google analytics
extensions.append('sphinxcontrib.googleanalytics')
googleanalytics_id = 'UA-82627369-1'


# SCVersioning.
scv_banner_greatest_tag = True
scv_grm_exclude = ('.gitignore', '.nojekyll', 'circle.yml', 'README.rst')
scv_overflow = ('-W',)
scv_show_banner = True
scv_sort = ('semver', 'time')
