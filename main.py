# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# def request_av():
    # requests.get方法
    # r = requests.get("https://www.baidu.com")
    # print("状态码：", r.status_code)

# Press the green button in the gutter to run the script.

"""
if __name__ == "__main__": 的核心目的是：
• 区分模块被导入使用 和 模块被直接运行 两种场景；
• 让模块既可以作为独立程序运行，也可以作为可复用模块被其他文件导入，实现 “一物两用”。

二、底层原理（为什么能生效？）
Python 解释器在运行一个 .py 文件时，会自动给这个文件设置一个内置变量 __name__：
当文件被直接运行时：__name__ 的值会被设为字符串 "__main__"；
当文件被作为模块导入时：__name__ 的值会被设为模块的文件名（比如 calc.py 被导入时，__name__ = "calc"）。
"""
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


