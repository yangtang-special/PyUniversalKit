from PyUniversalKit import Netkit
from ..Manage import Manage
import re


class Icodef():

    # 初始化添加匹配规则
    def __init__(self):
        self.url = "https://cx.icodef.com/v2/answer"


    @staticmethod
    def __parameterList(param):
        data = {
            "topic[0]":"%s"%param
        }
        return data

    @staticmethod
    def iterator(end_num):
        num = 0
        while num < end_num:
            yield num
            num += 1

    def _icodef(self,Q_list:list,cookie:str) -> list:
        """

        :param Q_list: List of questions extracted from the page
        :param cookie: User input or default cookie
        :return: Type of PrettyTable Object

        * 慕课小工具 Interface ,Project address:`https://cx.icodef.com/query.html?`

        """

        # _return_list is a [[]] list type
        _return_list:list = []

        for each_q in Q_list:
            # -----start define-----
            _Standard_answer:list = []

            # Find the range of text
            Scope = len(each_q)

            # Options
            _option: str = ""

            # Content
            _content: str = ""

            # Indent
            indentation = 1/3

            # -----end define-----

            """
            Search for the incoming data, the search result is empty or
            error will be repeated three times, each time reducing the current data
            If there is no result after three attempts, it will be skipped automatically.
            """

            for loop in self.iterator(3):
                data = self.__parameterList(each_q[0:Scope])
                try:
                    anwser = Netkit.post(url=self.url, cookie=cookie, data=data).json[0]["result"][0]
                    for each_simple_anwser in anwser["correct"]:

                        if type(each_simple_anwser["option"]) == bool:
                            flag = str(each_simple_anwser["option"])
                            _option += flag
                            _content += anwser["topic"]
                        elif "<img" in each_simple_anwser["content"]:
                            _option += each_simple_anwser["option"]
                            reg = r'src="(.*?)"'
                            result = "https://cx.icodef.com%s"%"".join(re.findall(reg,each_simple_anwser["content"]))
                            _content += "[%s]"%result
                        else:
                            _option += each_simple_anwser["option"]
                            if each_simple_anwser["content"] == "":
                                _content = "None"
                            else:
                                _content += "%s,"%each_simple_anwser["content"]

                    _content = re.sub('<[^<+]+?>', '', _content)
                    for (key, val) in Manage().replace_rules_f.items():
                        _content = _content.replace(key, val)
                    break

                except:
                    if loop < 3:
                        Scope = int(indentation * Scope)
                        continue
                    else:
                        anwser = "Format not supported or search error"
                        _option = anwser
                        _content = anwser

            _return_list.append(["%s"%each_q,_option, _content])


        return _return_list