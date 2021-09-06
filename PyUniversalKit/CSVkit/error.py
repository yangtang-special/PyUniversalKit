
class CSVkitInputTypeError(Exception):
    def __init__(self,_errorInput):
        Exception.__init__(self)
        self._errorMessage = _errorInput
    def __str__(self):
        return "输入数据 %s 的类型与函数要求所冲突"%self._errorMessage







class CSVkitImportError(Exception):
    def __init__(self,_packageName):
        Exception.__init__(self)
        self._packageName = _packageName
    def __str__(self):
        return "CSVkit所依赖的包 %s 未安装 \n" \
               "可以使用豆瓣源进行快速安装:  pip3 install -i https://pypi.doubanio.com/simple/ %s"%(self._packageName,self._packageName)