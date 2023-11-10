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
