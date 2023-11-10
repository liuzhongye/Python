"""
一、演示函数的多返回值示例
"""


# 演示使用多个变量，接收多个返回值
def test_return():
    return 1, "hello", True


x, y, z = test_return()
print(x)
print(y)
print(z)

"""
二、演示多种传参的形式
关键字参数
"""


def user_info(name, age, gender):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")


# 位置参数 - 默认使用形式
user_info('小明', 20, '男')

# 关键字参数
user_info(name='小王', age=11, gender='女')
user_info(age=10, gender='女', name='潇潇')  # 可以不按照参数的定义顺序传参
user_info('甜甜', gender='女', age=9)


# 缺省参数（默认值）
def user_info(name, age, gender):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")


user_info('小天', 13, '男')


# 不定长 - 位置不定长, *号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)}，内容是:{args}")


user_info(1, 2, 3, '小明', '男孩')


# 不定长 - 关键字不定长, **号
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)}，内容是:{kwargs}")


user_info(name='小王', age=11, gender='男孩')

"""
三、函数作为参数

"""


# c代表是形参
def test_func(compu):
    result = compu(2, 2)  # compu是一个函数的调用
    print(f"compu参数的类型是：{type(compu)}")
    print(result)


def compute(x, y):
    return x + y


# 测试把函数作为参数传递，这里传递的是实参
test_func(compute)

"""
函数compute，作为参数，传入了test_func中使用
test_func 需要一个函数作为参数传入，这个函数需要接收2个数字进行计算，计算逻辑有这个被传入函数决定
compute函数接收2个数字对其进行计算，compute函数作为参数，传递给了test_func函数使用
最终，在test_func函数内部，由传入的compute函数，完成了对数字的计算操作
所以，这是一种，计算逻辑的传递，而非数据的传递

"""

"""
四、函数的定义中由2种方式

1.def 关键字
2.lambda关键字
语法：lambda 传入参数：函数体（一行代码）

"""
test_func(lambda x, y: x + y)
