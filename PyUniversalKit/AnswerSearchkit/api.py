from .operate import QSobject
from .error import ApiTypeError
from .Manage import Manage
from .Models.AnswerObject import AnswerObject
from PyUniversalKit.version import current_version
from .API import get_all
from PyUniversalKit.AnswerSearchkit import CookieManager
from colorama import Fore



def search(url:str,**kwargs) -> AnswerObject:
    """

    :param url: Str
    :param kwargs: API:Str cookie:Str
    :return: PrettyTable Object

    * The search() method contains one required parameter url, optional parameters API (the source of the search API)


    """
    # Make default settings
    if 'API' not in kwargs:
        kwargs.setdefault("API",get_all()[0])
    if 'cookie' not in kwargs:
        kwargs.setdefault("cookie",__cookie(url=url))

    # Verify that the API interface is supported
    if kwargs["API"] not in Manage().api_support:
        raise ApiTypeError(kwargs["icodef"])
    print(Fore.LIGHTBLUE_EX + "You are using AnswerSearchkit {}, please wait for the program to finish...".format(current_version))
    return QSobject().search_question(url,**kwargs)


def __cookie(url:str) -> str:
    flag = CookieManager.search(PATH=url)
    if flag == False:
        print(Fore.RED + "\nHint: No cookies were found for this URL\n")
        return ""
    else:
        print(Fore.LIGHTGREEN_EX + "\nGet Cookie Success\n")
        return flag
