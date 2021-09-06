from .api import search
from .Structs import Matches,Mapping
from .Manage import Manage
from PyUniversalKit.version import current_version
from . import CookieManager


__all__ = ["search","version","Manage","Matches","Mapping","CookieManager"]

def version():
    return current_version













