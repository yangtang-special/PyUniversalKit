from PyUniversalKit import Netkit,CSVkit
from .Manage import Manage
from .Structs.Matches import Matches
from PyUniversalKit.Netkit.models import TestResponse
from .Models.AnswerObject import AnswerObject
from .error import MatchError,ApiTypeError,MatchTypeError,ThirdPackageImportError
from typing import Dict
import re
from colorama import Fore
try:
    from lxml import etree
except:
    raise ThirdPackageImportError("lxml")

__APITXT__ = "PyUniversalKit/AnswerSearchkit/Static/Template/API.txt"
__CONTENT__ = "PyUniversalKit/AnswerSearchkit/API/content.csv"



class QSobject():
    def search_question(self,url:str,**kwargs):

        def __all_rule_s() -> str:
            return "|".join(Manage().replace_rules_s)


        def __data_filtering_s(input_str: str, rule: str) -> str:
            get_removed = re.findall(rule, input_str)
            if len(get_removed) == 0:
                return input_str
            else:
                for i in get_removed:
                    input_str = input_str.replace(i, "")
                return input_str

        def __get_Q_list(which: Dict, add_list: list,url_response:TestResponse) -> list:
            add_list.clear()
            kind = which["kind"]
            reg = which["reg"]
            if kind == "RE":
                # RE Type Matching Rules
                url_result = re.findall(reg, url_response.text)
                for each_result in url_result:
                    to_string = "".join(each_result[:])
                    drop_html = re.sub('<[^<+]+?>', '', to_string)
                    # First data filtering rules
                    for (key, val) in Manage().replace_rules_f.items():
                        drop_html = drop_html.replace(key, val)

                    # Second data filtering rules
                    sec_data_filtering = __data_filtering_s(input_str=drop_html,rule=__all_rule_s())

                    add_list.append(sec_data_filtering)
                return add_list
            elif kind == "XPATH":
                # XPATH Matching Rules
                url_response = Netkit.get(url=url).text
                to_html = etree.HTML(url_response)
                url_result = to_html.xpath(reg)
                for each_result in url_result:
                    to_string = "".join(each_result[:])
                    drop_html = re.sub('<[^<+]+?>', '', to_string)

                    # First data filtering rules

                    for (key, val) in Manage().replace_rules_f.items():
                        drop_html = drop_html.replace(key, val)

                    add_list.append(drop_html)
                return add_list

            # Here you can add the corresponding data extraction method for the new match type
            else:

                raise MatchTypeError(kind, reg)




        API_type = kwargs["API"]
        cookie = kwargs["cookie"]

        # Call the properties of the match rule class to get all supported match rules
        Matchs = Matches().return_all_match

        # Get HTML resource objects with the Net Toolkit
        url_response = Netkit.get(url=url,cookie=cookie)

        # Iterate through all the rules, break when a rule is feasible, compose
        # a list of filtered data and pass it to the _icodef function, which will
        # iterate through and search that list

        for every_matches in Matchs:
            # Return List
            return_match_list = __get_Q_list(which=every_matches,add_list=[],url_response=url_response)
            if len(return_match_list) == 0 or "" in return_match_list:
                pass
            else:
                if API_type in Manage().api_support:

                    # No delete
                    Anwser_list = []

                    with open(__APITXT__,"r") as f:
                        need_to_run = f.read()%(API_type,API_type[1:],API_type[1:],API_type)
                    exec(need_to_run)
                    print(Fore.LIGHTGREEN_EX + "\nWrite file successfully")
                    contents = CSVkit.read(PATH=__CONTENT__).specifyROW()
                    return AnswerObject(_content=contents, _kind="icodef")
                else:
                    raise ApiTypeError(API_type)
        else:
            raise MatchError(_url=url)











