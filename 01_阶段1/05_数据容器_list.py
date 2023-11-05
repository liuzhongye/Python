"""
数据容器:一种可以容纳多份数据的数据类型，容纳的每一份数据称之为1个元素
每一个元素可以是任意类型的数据，如字符串、数字、布尔

数据容器根据特点不同，如：
-是否是指元素重复
-否可以修改
-是否有序
分为5类:
列表（list）、元组（tuple）、字符串（str）、集合（set）、字典（dict）
"""
# 一、list列表
# 语法：[元素,元素...]

name_list = ["java", "python", "c++"]
print(name_list)
print(type(name_list))  # <class 'list'>

# 列表可以一次性存储多个数据，且可以为不同的数据类型，支持嵌套
my_list = ["java", True, 666, ["1", "2", "3"]]
print(my_list)
print(type(my_list))

# 列表的下标索引取出列表的值,从0开始
print(name_list[0])  # java
print(name_list[1])  # python
print(name_list[2])  # c++
# print(name_list[3])  # IndexError: list index out of range

# 也可以反向取索引，也就是从后向前：从-1开始，依次递减。
# 倒数第一个元素是-1，倒数第二个是-2，一次递减
print(name_list[-1])  # c++
print(name_list[-2])  # python
print(name_list[-3])  # java

# 如果是嵌套的列表，同样支持下表索引
two_list = [["hi", "world"], ["你好", "世界"]]

# 取出'你好'这个元素
print(two_list[1][0])

# 列表的常用功能(方法)
demo_list = ["java", "go", "python"]
# 1 查询某元素的下表
index = demo_list.index("go")
print(index)

# 2 修改特定下表索引的值
demo_list[0] = "java被修改了"
print(demo_list)

# 3.在指定位置插入元素
# 在列表1的位置插入best
demo_list.insert(1, "best")
print(demo_list)

# 4 在列表尾部追击单个元素
demo_list.append("hello")
print(demo_list)

# 5 在列表尾部追击一批元素 extend(其他的数据容器)
demo_list.extend(["1", "2", "3"])
print(demo_list)

# 6 删除指定下表索引的元素
demo_list2 = ['java', 'best', 'go', 'python', 'hello', '1', '2', '3']

# 6.1 方式一 ：del 列表[下标]
del demo_list2[0]
print(demo_list2)
# 6.2 方式二：列表.pop(下标)
element = demo_list2.pop(0)
print(f"被删除的元素是{element}")
print(demo_list2)

# 7 删除某元素在列表中的第一个匹配项
demo_list3 = ['java', 'c#', 'java', 'python', 'hello']
demo_list3.remove("java")
print(f"通过remove方法移除元素后，列表的结果：{demo_list3}")

# 8 清空列表
demo_list3.clear()
print(f"通过clear方法清空元素后，列表的结果：{demo_list3}")

# 9 统计列表内全部的元素数量  列表.count(被统计的元素)
demo_list3 = ['java', 'c#', 'java', 'java', 'hello']
count = demo_list3.count("java")
print(f"列表中java的数量：{count}")

# 10 统计列表内总共有多少元素 len(列表)
print(f"列表中所有元素的数量：{len(demo_list3)}")

# 11 whiel遍历
"""
循环控制变量通过下标索引控制，默认0
每次循环都将下标索引变量+1
循环条件：下表索引<列表的元素数量
"""
i = 0
while i < len(demo_list3):
    element = demo_list3[i]
    print(f"while 遍历的元素：{element}")
    #至关重要，将循环变量增加1
    i += 1
print(f"while 遍历结束")

# 12 for 遍历
"""
for 临时变量 in 要遍历的数据：
    将临时变量进行操作
    
意义：将要遍历的数据的每一个元素赋予临时变量。
"""
for x in demo_list3:
    print(f"for 遍历：{x}")
    i += 1
print(f"for 遍历结束")

# 总结：
# while循环适用于任何想要循环的场景
# for 循环适用于容器遍历的场景或者固定次数的场景


