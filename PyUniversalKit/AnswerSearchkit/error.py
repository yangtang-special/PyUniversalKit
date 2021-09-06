


class ApiTypeError(Exception):
    def __init__(self,_error_str):
        self._error_str = _error_str
    def __str__(self):
        return "API接口 %s 暂时不被支持"%self._error_str

class MatchError(Exception):
    def __init__(self,_url):
        self._url = _url
    def __str__(self):
        return "该网址 %s 暂无可用匹配规则"%self._url

class ThirdPackageImportError(Exception):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "AnswerSearchkit所依赖的第三方库 %s 导入失败，请查明错误原因。\n若未下载，可以使用" \
               "豆瓣源进行快速安装:  pip3 install -i https://pypi.doubanio.com/simple/ %s"%(self.name,self.name)

class MatchTypeError(Exception):
    def __init__(self,kind,rule):
        self.kind = kind
        self.rule = rule
    def __str__(self):
        return "规则 %s 对应的种类 %s 不受支持"%(self.rule,self.kind)

class AdminRunError(Exception):
    def __init__(self,api,detail):
        self.api  = api
        self.detail = detail
    def __str__(self):
        return "重载API映射 %s 出现错误\n可能原因:\n1.未注册映射\n2.重载映射出错。\n详细原因:%s"%(self.api,self.detail)

class AdminStyleError(Exception):
    def __init__(self,api):
        self.api  = api
    def __str__(self):
        return "API %s 映射的表与实际数据格式相冲突"%self.api