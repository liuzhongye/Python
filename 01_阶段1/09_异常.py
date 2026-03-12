"""
当我们的程序遇到了BUG，那么接下来有两种情况:
整个程序因为一个BUG停止运行
对BUG进行提醒，整个程序继续运行

捕获异常的作用在于:提前假设某处会出现异常，做好提前准备，当真的出现异常的时候，可以有后续手段。

1.基本语法：
try:
    可能发送错误的代码
except:
    捕获异常
"""

# case1
# try:
#     f = open("C:\me.txt", "r", encoding="UTF-8")
# except:
#     print("出现异常了,无法打开文件")

# 2.捕获指定的异常
try:
    print(name)
except NameError as e:
    print("出现了未定义异常")
    print(e)
else:
    print("我是else,是没有异常的逻辑")
finally:
    print("我是finally逻辑")


# 3.捕获多个异常
try:
    print(name)
except (NameError,EOFError) as e:
    print("出现了未定义异常")
    print(e)


"""
Python 的模块（Module）是组织代码的核心方式，简单来说，模块就是一个包含 Python 定义和语句的 .py 文件，它能帮你把代码拆分成可复用、易维护的单元。
Python 模块的导入语法：[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

[from 模块名]：可选部分，用来指定 “从哪个模块里导入”，不写就代表直接导入整个模块。
import：核心关键字，意思是 “导入”。
[模块 | 类 | 变量 | 函数 | *]：要导入的具体内容：
可以是整个模块
可以是模块里的类、变量、函数
* 代表导入模块里所有公开内容
[as 别名]：可选部分，给导入的内容起一个简短好记的别名，方便代码书写。

日常开发推荐：
导入整个模块：import 模块名 as 别名
导入部分功能：from 模块名 import 功能名 as 别名
尽量避免：from 模块名 import *，除非是快速测试脚本。
"""

import math
print(math.sqrt(16))  # 调用math模块里的平方根函数

import  time
time.sleep(5)


"""
自定义模块 的导入

"""
import my_module_test
print(f"结果：{my_module_test.test(2,3)}")


"""
Python 的包（Package） 是比模块（Module）更高层级的代码组织方式，简单来说：包是一个包含 __init__.py 文件的文件夹，里面可以放多个 .py 模块文件，甚至嵌套子包。
它的核心作用是把相关的模块归类管理，让大型项目的代码结构更清晰、更易维护。
"""
# 方式一：
# import my_package.my_moudl1
# import my_package.my_moudlle2
# #
# my_package.my_moudl1.f_info1()
# my_package.my_moudlle2.f_info2()


#  方式二：from的导入方式
# from my_package import my_moudl1
# from my_package import my_moudlle2
#
# my_moudl1.f_info1()
# my_moudlle2.f_info2()

# 方式三 可以直接导入函数
from my_package.my_moudlle2 import f_info2
f_info2()
from my_package.my_moudl1 import f_info1
f_info1()

"""
第三方的包
使用pip命令安装第三方的包
"""