# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

#import logging
#logging.basicConfig(level=logging.DEBUG)


import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('..')))

# -- Project information -----------------------------------------------------

project = 'scikit-normod'
copyright = '2024, rd'
author = 'rd'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    #"sphinx-prompt",
    "sphinx_gallery.gen_gallery",
    #"numpydoc",
    "sphinx_design",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "literal"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

#html_theme = 'alabaster'
html_theme = 'pydata_sphinx_theme'
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'furo'
#html_theme = "sphinxawesome_theme"

html_css_files = [
    "css/project-template.css",
]

html_context = {
    "doc_path": "doc",
}

# -- Options for autodoc ------------------------------------------------------

autodoc_default_options = {
    "members": True,
    "inherited-members": True,
}

# generate autosummary even if no references
autosummary_generate = True

# -- Options for numpydoc -----------------------------------------------------

# this is needed for some reason...
# see https://github.com/numpy/numpydoc/issues/69
numpydoc_show_class_members = False


# -- Options for intersphinx --------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/{.major}".format(sys.version_info), None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "scikit-learn": ("https://scikit-learn.org/stable", None),
    "matplotlib": ("https://matplotlib.org/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "joblib": ("https://joblib.readthedocs.io/en/latest/", None),
}


# -- Options for sphinx-gallery -----------------------------------------------

plot_gallery = True

sphinx_gallery_conf = {
     "doc_module": "sknormod",
     "backreferences_dir": os.path.join("generated"),
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
     'download_all_examples': False,
     "reference_url": {"sknormod": None},
    # 'show_memory': True,
}


