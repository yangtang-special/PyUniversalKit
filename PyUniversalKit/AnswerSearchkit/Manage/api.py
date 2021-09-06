from ..API import get_all as return_all_api
from colorama import Fore


class Manage(object):
    def __init__(self):
        # First data filtering rules
        self.replace_rules_f = {
            "\n": "",
            "&nbsp;": "",
            " ": "",
            "(单选题)": "",
            "(多选题)": "",
            "(填空题)": "",
            "(判断题)": "",
            "[判断题]": "",
            "(简答题)": "",
            "(计算题)": "",
            "(单选题,": "",
            "(单选题": "",
            "(其它)": "",
            "(10分)": "",
            "10分)": "",
            "10分": "",
            "简答题": "",
            "(简答题": "",
            "*": "",
            "&": "",
            "@": "",
            "(": "",
            ")": "",
            # Add more rules here to

        }

        # Second Data Screening Rules
        # Initialize add matching rules
        self.replace_rules_s = [
            # Matching formats such as (1)
            r'[(（]/d+[)）]',
            # Matches such as 1. 1:
            r'\d+[.。:]',

        # You can add more ...
        ]

    @property
    def api_support(self) -> list:
        return return_all_api()

    @staticmethod
    def add_api(name:str):
        new_api_path = "PyUniversalKit/AnswerSearchkit/API/%s.py"%name
        try:
            with open("PyUniversalKit/AnswerSearchkit/Static/Template/template.txt", "r") as f:
                content = f.read() % (name.capitalize(), name)
            with open(new_api_path, 'w+') as f2:
                f2.write(content)
            print(Fore.LIGHTGREEN_EX + "The API interface file was created successfully (%s)\n Please register the mapping Table before using it."%new_api_path)
        except Exception as e:
            print(Fore.RED + "error:%s"%str(e))





