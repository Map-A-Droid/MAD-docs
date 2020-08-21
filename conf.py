import guzzle_sphinx_theme

project = u'MAD'
copyright = u'2020, MADdev Team'
version = u''
templates_path = ['_templates']
master_doc = 'index'
extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'guzzle_sphinx_theme',
    'sphinx.ext.autosectionlabel'
]

source_suffix = ['.rst', '.md']
source_parser = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

exclude_patterns = ['_build', 'venv', 'README.md']

html_theme = 'guzzle_sphinx_mad_theme'
html_theme_path = ['_themes',]
html_static_path = ['_static']
html_short_title = 'MAD Docs'
html_title = 'Map-A-Droid Documentation'
html_logo = "_static/mad_banner_trans.png"
html_theme_options = {
    'project_nav_name': 'Map-A-Droid',
    'globaltoc_depth': 4,
    'globaltoc_collapse': True
    }
html_sidebars = {
  '**': ['logo-text.html', 'searchbox.html', 'globaltoc.html']
}

# Define any toctree depth overrides that needs to be customized on a page
custom_depths = {
    'extras/integrations': 3,
    'faq': 2,
    'installation/security/index': 2,
    'madmin/index': 2,
    'madmin/auto_config': 3
}

html_context = {
    'custom_depths': custom_depths
}
