# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {".rst": "restructuredtext"}

# The master toctree document.
master_doc = "index"

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

# -- Options for autosummary extension ---------------------------------------
autosummary_generate = True
autosummary_imported_members = True
# If __all__ is defined document what is in __all__ and nothing else.
# If imported modules are in __all__ they are documented, whatever
# autosummary_imported_members.
autosummary_ignore_module_all = False

