from PyUniversalKit import CSVkit
from prettytable import PrettyTable
from typing import Union
import re

PATH_f = "PyUniversalKit/AnswerSearchkit/CookieManager/cookies.csv"
__all_cookie__ = [i for i in CSVkit.read(PATH_f).specifyROW()[1:] if i[2] == "True"]

def __rules():
    """
    ========= ================
    Code       Meaning
    --------- ----------------
    '000'     cookie不存在
    '001'     cookie存在一个
    '011'     cookie存在一个以上
    ========= ================

    :return: None
    """
    pass

def Add_Cookie(URL:str,COOKIE:str) -> bool:
    URL = __get_header(__translate(URL))
    COOKIE = __translate(COOKIE)
    if __existence(PATH=URL) == "000":
        if CSVkit.write(PATH=PATH_f, header=False, rows=[[URL, COOKIE,"True"]], Writing_method="a+"):
            return True
        else:
            return False
    else:
        return False

def __existence(PATH:str) -> str:
    return_list = [i[1] for i in __all_cookie__ if i[0] == PATH]
    if len(return_list) == 1:
        return '001'
    elif len(return_list) == 0:
        return '000'
    else:
        return '011'

def revise(PATH:str,COOKIE:str) -> bool:
    PATH = __get_header(__translate(PATH))
    COOKIE = __translate(COOKIE)
    if __existence(PATH=PATH) == "001":
        new_all = [['URL(Header)','cookie','state']]
        for i in __all_cookie__:
            new_all.append(i)
        pop_cookie = search(PATH=PATH)
        other_list = []
        for n in new_all:
            if n[1] == pop_cookie:
                other_list.append([n[0],COOKIE,n[2]])
            else:
                other_list.append([n[0],n[1],n[2]])
        if CSVkit.write(PATH=PATH_f, header=False, rows=other_list, Writing_method="w+"):
            return True
        else:
            return False
    else:
        return False

def search(PATH:str) -> Union[str,bool]:
    # There may be multiple values
    PATH = __get_header(__translate(PATH))
    if __existence(PATH=PATH) == "001":
        return [__retranslate(i[1]) for i in __all_cookie__ if i[0] == PATH][0]
    else:
        return False

def preview() -> PrettyTable:
    table = PrettyTable(['URL(Header)','cookie','state'])
    news = [["%s..."%__retranslate(i[0])[0:30],"%s..."%__retranslate(i[1])[0:30],i[2]] for i in __all_cookie__]
    table.add_rows(news)
    return table

def __translate(PATH:str) -> str:
    PATH = PATH.replace(",","@CookieManager")
    return PATH


def __retranslate(PATH:str) -> str:
    PATH = PATH.replace("@CookieManager",",")
    return PATH

def __get_header(url:str) -> str:
    reg = r'https://(.*?)/|http://(.*?)/'
    header = re.findall(reg, url)[0]
    return "".join(header)