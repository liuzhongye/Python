"""
演示以数据容器的角色，学习字符串的相关操作
"""
my_str = "I am a Chinese"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-7]
print(f"从字符串{my_str}取下标为2的元素，。值是：{value},取下标为-16的元素。值是：{value2}")

# 字符串不支持修改，也是只读的。
# my_str[2] = "H"  TypeError: 'str' object does not support item assignment

# index方法
value = my_str.index("am")
print(f"在字符串{my_str}中查找and，其起始下标是：{value}")

# 替换： replace方法 不会修改而是得到一个新的str
new_my_str = my_str.replace("Chinese", "student")
print(f"将字符串{my_str}，进行替换后得到：{new_my_str}")

# 分割 split方法
my_str = "hello python Qunar Qunar"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list}, 类型是：{type(my_str_list)}")

# 规整操作 strip()方法
my_str = "  itheima and itcast  "
new_my_str = my_str.strip()  # 不传入参数，去除首尾空格
print(f"字符串{my_str}被strip后，结果：{new_my_str}")

# 规整操作 strip(去前后指定的字符串)方法
my_str = "12qunar and Ctrip21"
new_my_str = my_str.strip("12")
# 这里会把12分隔，分成"1" "2",即去除12，或者21
print(f"字符串{my_str}被strip('12')后，结果：{new_my_str}")

# 统计字符串中某字符串的出现次数, count
my_str = "qunar and qunar"
count = my_str.count("ar")
print(f"字符串{my_str}中it出现的次数是：{count}")
# 统计字符串的长度, len()
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")
