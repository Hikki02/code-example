# settings/__init__.py
from split_settings.tools import optional, include

# Load the base settings
include('base.py')

# Load the environment-specific settings
include(
    optional('development.py'),
    optional('production.py'),
)
