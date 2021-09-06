from typing import Dict





class Matches(object):
    def __init__(self):
        # Custom rules need to be added to this again
        self.all_return = [self.__general(),self.__discussion_1(),self.__discussion_2()]

    @staticmethod
    def __general() -> Dict:
        kind = "RE"
        reg = r'<h3 class="mark_name colorDeep">([\S\s]*?)</h3>'
        reg_dict = {
            "kind":kind,
            "reg":reg
        }
        return reg_dict

    @staticmethod
    def __discussion_1() -> Dict:
        kind = "RE"
        reg = r'"content":"(.*?)"'
        reg_dict = {
            "kind": kind,
            "reg": reg
        }
        return reg_dict

    @staticmethod
    def __discussion_2() -> Dict:
        kind = "RE"
        reg = r'"title":"(.*?)"'
        reg_dict = {
            "kind": kind,
            "reg": reg
        }
        return reg_dict

    # Add new matching rules here (via decorators)


    @property
    def return_all_match(self) -> list:
        return self.all_return
