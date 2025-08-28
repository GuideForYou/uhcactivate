# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))


# -- Project information -----------------------------------------------------

project = 'Set Up VIZIO Account'
copyright = '2025, VIZIO'
author = 'VIZIO Support Team'
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# List of Sphinx extensions (add more if needed)
extensions = []

# Enable raw HTML in reStructuredText files
raw_enabled = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']  # Uncomment if using custom templates

# List of patterns to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML pages (change if preferred)
# html_theme = 'sphinx_rtd_theme'  # Uncomment if using Read the Docs theme

# Page metadata
html_title = "How to Set Up a VIZIO Account – Complete Guide"
html_short_title = "VIZIO Setup Guide"

# Favicon (put your favicon.ico in _static or root folder)
html_favicon = 'favicon.ico'

# Hide the "View page source" link
html_show_sourcelink = False

# Allow unsafe/raw HTML usage inside .rst files
html_allow_unsafe = True

# Theme customization options (only works with some themes)
html_theme_options = {
    'show_powered_by': False,
}

# Static file path (uncomment if using custom CSS/images)
# html_static_path = ['_static']
