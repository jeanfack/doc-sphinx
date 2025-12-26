# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Jean Fack documentation'
copyright = '2025, Jean Fack'
author = 'Jean Fack'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# https://www.sphinx-doc.org/en/master/usage/markdown.html
# https://github.com/MrDogeBro/sphinx_rtd_dark_mode
extensions = [
    'myst_parser', # https://myst-parser.readthedocs.io
    'sphinx_rtd_theme', # https://sphinx-rtd-theme.readthedocs.io
    #'sphinx_rtd_dark_mode', # https://github.com/MrDogeBro/sphinx_rtd_dark_mode
    'sphinxcontrib.mermaid', # https://github.com/mgaitan/sphinxcontrib-mermaid
    'sphinx_design', # https://sphinx-design.readthedocs.io
    'sphinx_copybutton', # https://sphinx-copybutton.readthedocs.io
    'sphinx.ext.githubpages', # https://sphinx-themed.readthedocs.io/en/latest/usage/extensions/githubpages.html
    'sphinx.ext.graphviz', # https://www.sphinx-doc.org/fr/master/usage/extensions/graphviz.html
    #'sphinx_immaterial', # https://github.com/jbms/sphinx-immaterial
    #'sphinx_immaterial.graphviz', # https://jbms.github.io/sphinx-immaterial/graphviz.html
] 

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "attrs_block",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

templates_path = ['_templates']
exclude_patterns = ['_include']


html_static_path = ['_static']


# html_theme = 'alabaster'
# html_theme = 'pydata_sphinx_theme'


# Pygments Style for code-block
pygments_style = 'github-dark'

graphviz_dot = 'C:\\Program Files\\Graphviz\\bin\\dot.exe'

##########################
#   MrDogeBro
##########################
"""
html_css_files = ['custom-sphinx_rtd_theme.css']

html_theme = 'sphinx_rtd_theme'

html_context = {
    'default_mode' : 'dark'
}

html_theme_options = {
    'navigation_depth': -1,
    'collapse_navigation': True
}

"""

##########################
#  Furo
##########################
html_css_files = ['custom-furo.css']

html_theme = 'furo' # https://pradyunsg.me/furo/

html_title = 'Jean Fack doc'


html_context = {
    'default_mode' : 'dark'
}


#html_theme_options = {
#    'sidebarwitdh': '840px',
#    'body_max_witdh': 'none'
#}
