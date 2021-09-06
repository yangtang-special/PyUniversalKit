from .operate import Operate
from .error import CSVkitInputTypeError
from typing import Union

def read(PATH:str,**kwargs) -> Operate():
    """

    :param PATH: Str
    :param kwargs: The incoming parameters are path [Reading_method:str,...]
    :return: Operate() Object
    """

    if 'Reading_method' not in kwargs:
        kwargs.setdefault("Reading_method","r")
    return Operate().read(PATH,**kwargs)

def write(PATH:str,header:Union[list,bool],rows:list,**kwargs) -> Operate():
    """
    :param PATH: Str
    :param header: Single-dimensional array -> []
    :param rows: Multidimensional Arrays -> [[Optional]]
    :param kwargs: [Writing_method:Bool,...]
    :return: Operate() Object

    ========= ======================================================================================================
    CSV       读写模式
    --------- ------------------------------------------------------------------------------------------------------
    'r'       打开只读文件 该文件必须存在
    'r+'      打开可读写的文件，该文件必须存在。
    'w'       打开只写文件，若文件存在则文件长度清为0，即该文件内容会消失。若文件不存在则建立该文件。
    'w+'      打开可读写文件，若文件存在则文件长度清为零，即该文件内容会消失。若文件不存在则建立该文件。
    'a'       以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。
    'a+'      以附加方式打开可读写的文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留。
    ========= ======================================================================================================

    Issues to note about this function

    * The only necessary parameters are the first three, see `operate.py` for
      details of how to operate the function.

    * This function returns an object of the operation type, processes the
      relevant data in the object's built-in functions and returns the
      WriteCSVobject object

    """

    if "Writing_method" not in kwargs:
        kwargs.setdefault("Writing_method","w+")

    if type(rows[0]) != list:
        raise CSVkitInputTypeError(rows)
    else:
        return Operate().write(PATH, header, rows, **kwargs)