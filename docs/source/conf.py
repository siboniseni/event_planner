import os
import sys
import django

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath("../.."))

# Set up Django settings module
os.environ["DJANGO_SETTINGS_MODULE"] = "event_planner.settings"
django.setup()

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Event Planner'
copyright = '2025, Siboniseni'
author = 'Siboniseni'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",       # Auto-generate documentation from docstrings
    "sphinx.ext.napoleon",      # Support for Google-style and NumPy docstrings
    "sphinx.ext.viewcode",      # Add links to source code
    "sphinx.ext.autosummary",   # Create summary tables for modules
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
