

"""
所有的定义对象
"""

#在Response类基础上
class TestResponse(object):
    def __init__(self,_content):
        self._content = _content

    @property
    def text(self):
        try:
            return self._content.text
        except Exception as e:
            return "error:%s"%str(e)

    @property
    def json(self):
        try:
            return self._content.json()
        except Exception as e:
            return "error:%s\nPossible reason:The data itself is not in json format"%str(e)

    @property
    def content(self):
        try:
            return self._content.content
        except Exception as e:
            return "error:%s"%str(e)

    @property
    def next(self):
        try:
            return self._content.next
        except Exception as e:
            return "error:%s"%str(e)

    @property
    def links(self):
        try:
            return self._content.links
        except Exception as e:
            return "error:%s"%str(e)





