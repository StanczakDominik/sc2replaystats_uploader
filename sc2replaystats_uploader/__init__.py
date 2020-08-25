"""Top-level package for sc2replaystats_uploader."""

__author__ = """Dominik Stańczak"""
__email__ = "stanczakdominik@gmail.com"

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
   pass
