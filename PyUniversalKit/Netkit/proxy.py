from PyUniversalKit import CSVkit,Netkit
from lxml import etree

class Proxy():
    def __init__(self):
        self.rules = {
            "XPATH":'//div[@class="container"]/div[@class="containerbox boxindex"]/div[@class="layui-row layui-col-space15"]/div[@align="center"]/table/tr/td/text()',
        }
    def _analysis_xpath(self,url:str,nums):
        rules = self.rules["XPATH"]
        url_response = Netkit.get(url=url,encoding="gb2312").text
        to_html = etree.HTML(url_response)
        list_ip = to_html.xpath(rules)
        num = len(list_ip[5:])
        last_list = []
        for i in range(0,num,5):
            try:
                last_list.append([list_ip[5:][i],list_ip[5:][i+1],list_ip[5:][i+2],list_ip[5:][i+3],list_ip[5:][i+4]])
            except IndexError:
                pass
        CSVkit.write(PATH="./static/proxies%s.csv"%nums,header=['ip','端口号','代理位置','代理类型','验证时间'],rows=last_list)


"""
    
    You can use the following function to get all the IPs in the url: http://www.66ip.cn/%s.html

    print("loading...")
    for j in range(2,2453):
        try:
            Proxy()._analysis_xpath(url='http://www.66ip.cn/%s.html' % j, nums=j)
        except:
            pass
        
"""


