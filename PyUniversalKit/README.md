# PyUniversalKit工具包

#### Hello,PyUniversalKit!

## 下载方式
> `pip install PyUniversalKit` 

## 支持
<a href="https://pypi.org/project/PyUniversalKit/"><img src="/Users/macos/Downloads/python_icon.svg"></a>

## 更新
* #### AnswerSearchkit新增Cookie管理器 
* #### 改进数据流操作结构，优化相应的方法和框架
* #### 提高了稳定性

## 工具包内容

* ## AnswerSearchkit
  #### AnswerSearchkit工具包是为了满足网页快速搜题需求。输入匹配规则以及url，将会自动获取该页面全部题目并提供搜索，目前提供search()一个方法
  ### 示例
  * #### 使用Manage创建新的API接口文件,以icodef为例
    > `Manage.add_api(name="icodef")`
  * #### 在对应的API文件里面编写相应逻辑函数
    <img src="PyUniversalKit/PIC/API.png">
  * #### 前往admin.py注册新API接口对应的映射Table
    <img src="PyUniversalKit/PIC/admin.png">
  * #### 如果有需要，使用Cookie管理器:CookieManager创建新Cookie;flag是一个BOOL值，为True的时候添加Cookie成功
    > `flag = CookieManager.Add_Cookie(URL="要访问的URL",COOKIE="对应的COOKIE")` 
  * #### 前往PyUniversalKit/AnswerSearchkit/Structs/Matches.py手动添加题目匹配规则（Xpath或者正则表达式）
  * #### 使用search函数获取待搜索界面答案(注意：在该模式下，AnswerSearchkit将会通过CookieManager自动查找相应的Cookie)
    > `anwserOBJ = AnswerSearchkit.search(url="要访问的URL",API="选择一个API")`
  * #### 在不通过CookieManager的情况下，可以手动输入cookie
    > `cookie = "你的Cookie"`
    > `anwserOBJ = AnswerSearchkit.search(url="要访问的URL",cookie=cookie,API="选择一个API")`
  * #### 此外，也可以不携带API参数，那么AnswerSearchkit将会使用API列表的第一个API作为默认API
    > `anwserOBJ = AnswerSearchkit.search(url="要访问的URL",cookie=cookie)`
  * #### anwserOBJ是一个AnswerObject类型的值，AnswerSearchkit为其提供了3个属性
    * #### 打印PrettyTable类型的表
    > `print(anwserOBJ.preview)`
    * #### 返回全部问题
    > `print(anwserOBJ.only_question)`
    * #### 返回包含问题和回答在内的源数据，列表类型
    > `print(anwserOBJ.original_data)`
  ### CookieManager
  * #### 新增cookie
    > `cookie_add = CookieManager.Add_Cookie(URL="XXX",COOKIE="XXX")`
  * #### 搜索cookie
    > `cookie_search = CookieManager.search(PATH="XXX")`
  * #### 预览所有的存储的Cookie，PrettyTable类型
    > `cookie_pre = CookieManager.preview()`
  * #### 修改cookie
    > `cookie_rev = CookieManager.revise(PATH="XXX",COOKIE="XXX")`
  * #### 此外，也可以通过修改位于PyUniversalKit/AnswerSearchkit/CookieManager/cookies.csv的文件来实现增删查改等功能
  
  ### Manage
  * #### 通过Manage增加API接口文件
    > `Manage.add_api(name="XXX")`
  * #### 获取所有接口文件
    > `All_api_list = Manage.api_support`
  * #### 此外可前往PyUniversalKit/AnswerSearchkit/Manage/api.py来更改数据筛选规则
  > * `from PyUniversalKit import Netkit,AnswerSearchkit`
  > * `result = AnswerSearchkit.search(url="XXX",**kwargs)`
  > * `print(result.preview)`
  
* ## CSVkit
  #### CSVkit工具包提供了多种便携的方法来操作CSV文件
  #### 提供方法：`read`，`write`,调用这两个方法会返回`CSVobjects`类型；
  #### 该类型主要属性有：
  * `.preview`: 返回一个*PrettyTable*格式的表，显示传入文件前1000行内容（不够1000行全部显示）
  * `.size`: 返回该文件的大小
  * `.modify_time`: 返回该文件的上次修改时间
  *  `.create_time`: 返回该文件的创建时间
  *  `.rows`: 返回文件的总行数
  *  `.columns`: 返回文件的总列数
  #### 主要方法有：
  * `specifyROW()`： 方法接受三个可选变量:start_num,end_num,equal，将会返回第start_num行与end_num行（不包括end_num）之间的CSV数据，若equal为True，end_num行的数据也会被返回
  #### 更多方法和属性的详细用法请阅读对应的*api.py*文件
  #### 示例
  >* `from PyUniversalKit import CSVkit`
  >* `csv_obj = CSVkit.read("/Users/macos/Downloads/2021zzuli模拟赛/C_hour.csv")`
  >* `print(csv_obj.specifyROW(start_num=3,end_num=4,equal=False))`
  >* `print(csv_obj.preview)`
  * 参数均为空的时候默认为0,all,True.
* ## Netkit
  #### 与requests库用法一致，自己去看源代码。
  
  
  ## 注意：本项目内置的API接口为<a href="https://github.com/CodFrm/cxmooc-tools">*超星慕课小工具*</a>,感谢这位创作者提供的接口
