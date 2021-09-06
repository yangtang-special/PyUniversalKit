from .error import CSVkitImportError
from time import time
try:
    from prettytable import PrettyTable
except:
    raise CSVkitImportError("prettytable")





class CSVobjects(object):
    def __init__(self,_content:list,_fileMessage:dict):
        """
        :param _content: The key Value-List of `func-op`
        """
        self._content = _content
        self._fileMessage = _fileMessage
        # 实际继承csv.reader()类
    @property
    def size(self):
        """
        :return: Byte

        * 1 MB = 1024 KB = 1048576 Bytes
        """
        return "%s Byte"%self._fileMessage["size"]


    @property
    def modify_time(self):
        return self._fileMessage["mtime"]

    @property
    def create_time(self):
        return self._fileMessage["ctime"]

    @property
    def rows(self) -> int or str:
        try:
            return len(self._content)
        except Exception as e:
            return "error:%s"%str(e)

    @property
    def columns(self) -> int or str:
        try:
            max = len(self._content[0])
            for each_row in self._content[1:]:
                if max < len(each_row):
                    max = len(each_row)
                else:
                    pass
            return max
        except IndexError:
            return "error:First row have no datas"

    @staticmethod
    def __get_iterator(start_value:int,end_value:int,equal:bool):
        if equal == True:
            while start_value <= end_value:
                yield start_value
                start_value += 1
        else:
            while start_value < end_value:
                yield start_value
                start_value += 1

    def specifyROW(self,**kwargs) -> str or list:
        """
        :param kwargs: start_num:int,end_num:int,equal:bool
        :return: List

        * When equal is true, data in the range `[start_num,end_num]` will be returned

        * When equal is False, data in the range `[start_num,end_num)` will be returned
        """
        if "start_num" not in kwargs:
            kwargs.setdefault("start_num",0)
        if "end_num" not in kwargs:
            kwargs.setdefault("end_num",len(self._content))
        if "equal" not in kwargs:
            kwargs.setdefault("equal",False)

        start_num = int(kwargs["start_num"])
        end_num = int(kwargs["end_num"])

        if start_num >= end_num:
            return "start_num '%s' must smaller than '%s" % (start_num, end_num)
        elif start_num < 0 or end_num < 0:
            return "input must bigger than 0 or it is 0."
        else:
            return_list:[] = []
            for i in self.__get_iterator(start_num,end_num,kwargs["equal"]):
                return_list.append(self._content[i])
            return return_list

    @property
    def preview(self):
        """
        :return: prettytable.prettytable.PrettyTable
        """
        start = time()
        header_length = len(self._content[0])
        # Calculate maximum width
        max = header_length
        for each_row in self._content[1:]:
            if max < len(each_row):
                max = len(each_row)
            else:
                pass
        # Setting the header
        Complete_header_list = self._content[0][:]
        if header_length == max:
            table = PrettyTable(Complete_header_list)
        else:
            Gaps = max - header_length
            for _ in self.__get_iterator(0, Gaps, False):
                Complete_header_list.append("")
            table = PrettyTable(Complete_header_list)
        # Completing every list but first header
        if len(self._content) > 1000:
            pre_num = 1000
        else:
            pre_num = len(self._content)
        for each_row_last in self._content[1:pre_num]:
            ready_to_add_row = each_row_last[:]
            if len(ready_to_add_row) < max:
                Gaps = max - len(ready_to_add_row)
                for _ in self.__get_iterator(0,Gaps,False):
                    ready_to_add_row.append("")
            else:
                pass
            table.add_row(ready_to_add_row)
        elapsed = (time() - start)
        print("Process ends after %s seconds,Range is the first %s rows"%(elapsed,pre_num))

        return table


class WriteCSVobject(CSVobjects):
    def __init__(self,_content:list,_fileMessage:dict,_path:str):
        CSVobjects.__init__(self,_content,_fileMessage)
        self._path = _path

    @property
    def path(self):
        return self._path



