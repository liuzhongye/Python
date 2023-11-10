"""
一、字典的定义，同样使用{}，不过元素是一个个键值对
{key:value,...key:value,key:value}
"""

# 1.定义字典
my_dict = {"王力宏": 99, "周杰伦": 100, "张三": 77}

my_dict2 = {}
my_dict3 = dict()

# 基于key获取value
score = my_dict["王力宏"]
print(f"王力宏考试分数是:{score}")

# 从字典中基于Key获取Value
my_dict1 = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}
score = my_dict1["王力鸿"]
print(f"王力鸿的考试分数是：{score}")
score = my_dict1["周杰轮"]
print(f"周杰轮的考试分数是：{score}")
# 定义嵌套字典
stu_score_dict = {
    "王力鸿": {
        "语文": 77,
        "数学": 66,
        "英语": 33
    }, "周杰轮": {
        "语文": 88,
        "数学": 86,
        "英语": 55
    }, "林俊节": {
        "语文": 99,
        "数学": 96,
        "英语": 66
    }
}
print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套字典中获取数据
# 看一下周杰轮的语文信息
score = stu_score_dict["周杰轮"]["语文"]
print(f"周杰轮的语文分数是：{score}")
score = stu_score_dict["林俊节"]["英语"]
print(f"林俊节的英语分数是：{score}")

"""
二、字典的常用操作
"""
my_dict5 = {"dpt": "PEK", "arr": "SHA", "dptDate": 20131205}

# 新增元素
my_dict5["retDate"] = 20231210
print(f"字典经过新增元素后，结果：{my_dict5}")
# 更新元素
my_dict5["dptDate"] = 20131206
print(f"字典经过更新后，结果：{my_dict5}")
# 删除元素
score = my_dict5.pop("retDate")
print(f"字典中被移除了一个元素，结果：{my_dict5}, 往返日期是：{score}")

# 清空元素, clear
my_dict5.clear()
print(f"字典被清空了，内容是：{my_dict5}")

# 获取全部的key
my_dict6 = {"dpt": "PEK", "arr": "SHA", "dptDate": 20131205}
keys = my_dict6.keys()
print(f"字典的全部keys是：{keys}")
# 遍历字典
# 方式1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是:{key}")
    print(f"字典的value是：{my_dict6[key]}")

# 方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict6:
    print(f"2字典的key是:{key}")
    print(f"2字典的value是：{my_dict6[key]}")

# 统计字典内的元素数量, len()函数
num = len(my_dict6)
print(f"字典中的元素数量有：{num}个")

"""
三、演示数据容器的通用功能
"""
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")

# max最大元素
print(f"列表 最大的元素是：{max(my_list)}")
print(f"元组 最大的元素是：{max(my_tuple)}")
print(f"字符串最大的元素是：{max(my_str)}")
print(f"集合 最大的元素是：{max(my_set)}")
print(f"字典 最大的元素是：{max(my_dict)}")
# min最小元素
print(f"列表 最小的元素是：{min(my_list)}")
print(f"元组 最小的元素是：{min(my_tuple)}")
print(f"字符串最小的元素是：{min(my_str)}")
print(f"集合 最小的元素是：{min(my_set)}")
print(f"字典 最小的元素是：{min(my_dict)}")
# 类型转换: 容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")
# 类型转换: 容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组结果是：{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是：{tuple(my_dict)}")
# 类型转换: 容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串结果是：{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是：{str(my_dict)}")
# 类型转换: 容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合结果是：{set(my_str)}")
print(f"集合转集合的结果是：{set(my_set)}")
print(f"字典转集合的结果是：{set(my_dict)}")
# 进行容器的排序
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "bdcefga"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5}

print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")

print(f"列表对象的反向排序结果：{sorted(my_list, reverse=True)}")
print(f"元组对象的反向排序结果：{sorted(my_tuple, reverse=True)}")
print(f"字符串对象反向的排序结果：{sorted(my_str, reverse=True)}")
print(f"集合对象的反向排序结果：{sorted(my_set, reverse=True)}")
print(f"字典对象的反向排序结果：{sorted(my_dict, reverse=True)}")

