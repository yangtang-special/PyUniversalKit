# PyUniversalKit Toolkit

#### Hello,PyUniversalKit!

## Download method
> `pip install PyUniversalKit` 

## Support
<a href="https://pypi.org/project/PyUniversalKit/"><img src="/Users/macos/Downloads/python_icon.svg"></a
<a href="https://pypi.org/project/PyUniversalKit/"><img src="https://img.shields.io/pypi/v/PyUniversalKit"></a

## Updates
* #### AnswerSearchkit adds Cookie Manager 
* #### Improved data flow manipulation structure and optimized the corresponding methods and framework
* #### Improved stability

## Toolkit contents

* ## AnswerSearchkit
  #### AnswerSearchkit toolkit is designed to meet the needs of web page quick search. If you enter the matching rules and the url, all the questions on the page will be automatically retrieved and search will be provided, currently a search() method is provided
  ### Example
  * #### Create a new API interface file using Manage, using icodef as an example
    > `Manage.add_api(name="icodef")`
  * #### Write the corresponding logic function in the corresponding API file
  * #### Go to admin.py to register the mapping Table corresponding to the new API interface
  * #### If necessary, use CookieManager:CookieManager to create a new cookie; flag is a BOOL value, True when the cookie is added successfully
    > `flag = CookieManager.Add_Cookie(URL="URL to visit",COOKIE="corresponding COOKIE")` 
  * #### Go to PyUniversalKit/AnswerSearchkit/Structs/Matches.py to manually add question matching rules (Xpath or regular expressions)
  * #### Use the search function to get the answer of the interface to be searched (note: in this mode, AnswerSearchkit will automatically find the corresponding cookie via CookieManager)
    > `anwserOBJ = AnswerSearchkit.search(url="URL to visit",API="Select an API")`
  * #### You can enter a cookie manually without passing CookieManager
    > `cookie = "Your Cookie"`
    > `anwserOBJ = AnswerSearchkit.search(url="URL to visit",cookie=cookie,API="Select an API")`
  * #### Alternatively, you can not carry the API parameter, then AnswerSearchkit will use the first API in the API list as the default API
    > `anwserOBJ = AnswerSearchkit.search(url="URL to visit",cookie=cookie)`
  * #### anwserOBJ is a value of type AnswerObject, for which AnswerSearchkit provides 3 properties
    * #### prints a table of type PrettyTable
    > `print(anwserOBJ.preview)`
    * #### returns all questions
    > `print(anwserOBJ.only_question)`
    * #### returns the source data including questions and answers, list type
    > ` print(anwserOBJ.original_data)`
  ### CookieManager
  * #### Add a new cookie
    > `cookie_add = CookieManager.Add_Cookie(URL="XXX",COOKIE="XXX")`
  * #### Search for cookies
    > `cookie_search = CookieManager.search(PATH="XXX")`
  * #### Preview all stored cookies, PrettyTable type
    > `cookie_pre = CookieManager.preview()`
  * #### Modify cookies
    > `cookie_rev = CookieManager.revise(PATH="XXX",COOKIE="XXX")`
  * #### In addition, you can also modify the file located in PyUniversalKit/AnswerSearchkit/CookieManager/cookies.csv to add, delete, check, change, etc.
  
  ### Manage
  * #### Add API interface file via Manage
    > `Manage.add_api(name="XXX")`
  * #### Get all interface files
    > `All_api_list = Manage.api_support`
  * #### Also go to PyUniversalKit/AnswerSearchkit/Manage/api.py to change the data filtering rules
  > * `from PyUniversalKit import Netkit,AnswerSearchkit`
  > * `result = AnswerSearchkit.search(url="XXX",**kwargs)`
  > * `print(result.preview)`
  
* ## CSVkit
  #### CSVkit toolkit provides a variety of portable methods to manipulate CSV files
  #### provides methods: `read`, `write`, calls to these two methods return the type `CSVobjects`.
  #### The main attributes of this type are.
  * `.preview`: returns a table in *PrettyTable* format, displaying the first 1000 lines of the incoming file (not all 1000 lines are displayed)
  * `.size`: returns the size of the file
  * `.modify_time`: returns the last modification time of the file
  * `.create_time`: returns the creation time of the file
  * `.rows`: Returns the total number of rows in the file
  * `.columns`: Returns the total number of columns in the file
  #### The main methods are.
  * `specifyROW()`: method accepts three optional variables: start_num,end_num,equal, will return the CSV data between the start_num row and the end_num row (excluding end_num), if equal is True, the data of the end_num row will also be returned
  #### For more detailed usage of methods and properties, please read the corresponding *api.py* file
  #### Example
  >* `from PyUniversalKit import CSVkit`
  >* `csv_obj = CSVkit.read("/Users/macos/Downloads/2021zzuli Simulation/C_hour.csv")`
  >* `print(csv_obj.specifyROW(start_num=3,end_num=4,equal=False))`
  >* `print(csv_obj.preview)`
  * Default is 0,all,True when all parameters are empty.
* ## Netkit
  #### Same usage as the requests library, see the source code for yourself.
  
  
  ## Note: The built-in API of this project is <a href="https://github.com/CodFrm/cxmooc-tools">*超星慕课小工具*</a>, thanks to this creator for providing the interface
 Translated with www.DeepL.com/Translator (free version)
