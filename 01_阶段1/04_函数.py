# 函数：是组织好的 可重复使用的，特定代码块
"""
def 函数名称（传入参数）:
    函数体
    return 返回值

例如前面用到的函数：
print()、int()、str()、input() 等等都是定义好的函数
len() 统计字符串的长度
"""
str1 = 'good good study day day up'
ser1_length = 0

for x in str1:
    if 'o' == x:
        ser1_length += 1
print(ser1_length)


# 定义函数def，统计o的次数
def count_len(data, length_l=0):
    for i in data:
        if 'o' == i:
            length_l += 1
    print(f"函数的长度:{length_l}")


# 调用定义的函数
count_len("good!")


# 带返回值的 使用return
def my_count(x, y):
    result = x + y
    print(f"{x}+{y}的结果：{result}")
    return result


# 调用定义的函数
my_count(2, 3)

# 无返回值的函数，实际返回了None 就是空、没有含义的意思
re_None = count_len("good")
print(type(re_None))  # <class 'NoneType'>

# 使用场景：
# 常用在if判断上，None等同于与false
if count_len("good"):
    print("222")
else:
    print("2222")


# 定义函数的说明文档。写在函数体前 用：param 的形式
def my_add(x, y, z):
    """
    my_add函数用于计算3个数字的和
    :param x: 第一个参数
    :param y: 第二个参数
    :param z: 第三个参数
    :return: 返回3数之和
    """
    result = x + y + z
    print(f"{x}+{y}+ {z}的结果：{result}")
    return result


my_add(1, 2, 3)

# 函数的局部变量和全局变量
# 局部变量:只在函数体内才生效的
# 全局变量:在函数体内体外都生效

"""
testb能把num的值修改成200吗？
如果不能该如何修改程序才能实现？
"""
# 全局变量
num = 200
def testa():
    print(f"testa:{num}")
def testb():
    num = 500
    print(f"testa:{num}")

testa()  # 200
testb()  # 500
print(num)  # 200

"""
需要global关键字才能完成
即在testb中修改成：global num = 500
global 关键字声明num是全局变量
"""
# 全局变量
num = 200
def testa():
    print(f"testa:{num}")
def testb():
    # global关键字声明num是全局变量
    global num
    num = 500
    print(f"testa:{num}")

testa()  # 200
testb()  # 500
print(num)  # 500
