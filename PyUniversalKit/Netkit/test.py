import requests
from .models import TestResponse
from typing import Union,Dict

class Test():
    def get(self,url:str,headers:Dict[str,Union[str,int,float,bytes]],encoding:str) -> Union[TestResponse,str]:
        try:
            response = requests.get(url=url, headers=headers)
            response.encoding = encoding
            return TestResponse(_content=response)
        except Exception as e:
            return "error:%s" % str(e)

    def post(self,url:str,data:Dict[str,Union[str,int,float,bytes]],headers:Dict[str,Union[str,int,float,bytes]],encoding:str) -> Union[TestResponse,str]:
        try:

            proxies = {
                "http": "http://82.114.93.210:8080"
            }
            response = requests.post(url=url, headers=headers, data=data,proxies=proxies)
            response.encoding = encoding
            return TestResponse(_content=response)
        except Exception as e:
            return "error:%s" % str(e)











