from . import test,USER_AGENT_LIST
from .models import TestResponse
from typing import Dict,Union

def get(url:str,**kwargs) -> TestResponse:
    """

    :param url: Str
    :param kwargs: encoding,cookie
    :return: TestResponse
    """
    if "encoding" not in kwargs:
        kwargs.setdefault("encoding", "utf-8")
    if "cookie" not in kwargs:
        kwargs.setdefault("headers", USER_AGENT_LIST.returnUA(None))
    else:
        kwargs.setdefault("headers", USER_AGENT_LIST.returnUA(kwargs["cookie"]))
        del kwargs["cookie"]

    return test.Test().get(url, **kwargs)


def post(url:str,data:Dict[str,Union[str,int,float,bytes]],**kwargs) -> TestResponse:
    """

    :param url: Str
    :param data: Dict
    :param kwargs: encoding,cookie
    :return: TestResponse
    """
    if "encoding" not in kwargs:
        kwargs.setdefault("encoding", "utf-8")
    if "cookie" not in kwargs:
        kwargs.setdefault("headers", USER_AGENT_LIST.returnUA(None))
    else:
        kwargs.setdefault("headers", USER_AGENT_LIST.returnUA(kwargs["cookie"]))
        del kwargs["cookie"]

    return test.Test().post(url, data, **kwargs)







