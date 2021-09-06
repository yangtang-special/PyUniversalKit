from .api import read,write
from PyUniversalKit.version import current_version


__all__ = ["read","write","version"]

def version():
    return current_version