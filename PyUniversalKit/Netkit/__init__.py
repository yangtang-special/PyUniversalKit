from .api import get,post
from PyUniversalKit.version import current_version


__all__ = ["get","post","version"]

def version():
    return current_version