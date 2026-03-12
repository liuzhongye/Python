"""
演示对文件的读取
"""

# 1.打开文件 r模式
import time

f = open("C:/Log/1.txt", "r", encoding="UTF-8")
print(type(f))
# 读取文件 - read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"read方法读取全部内容的结果是：{f.read()}")
# print("-----------------------------------------------")
# # 读取文件 - readLines()
# lines = f.readlines()   # 读取文件的全部行，封装到列表中
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# # 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")

# # for循环读取文件行
# for line in f:
#     print(f"每一行数据是:{line}")
# # # # 文件的关闭
# f.close()


# time.sleep(500000)
# with open() as f 语法操作文件 以后都推荐用这个.因为文件操作完毕后，就会自动close。
# with open("C:/Log/1.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         print(f"每一行数据是：{line}")

# time.sleep(500000)


# 练习统计MU5324航班的出现个数

f = open("C:/Log/2.txt", "r", encoding="UTF-8")

# 方式1
# content = f.read()
# count = content.count("MU5324")
# print(f"MU5324出现了{count}次")
# f.close()

# 方式2
# count  = 0
# for line in f:
#     line.strip()
#     words = line.split(" ")
#     for word in words:
#         if word != "MU5324":
#             continue
#         count += 1
#
# print(f"MU5324出现了{count}次")


# 2. 文件的写入操作 write   flush
"""
2.1使用open函数的"w"模式进行
2.2.写入的方法有:
wirte()，写入内容
flush()，刷新内容到硬盘中
2.3注意事项:
w模式，文件不存在，会创建新文件
w模式，文件存在，会清空原有内容，写入新文件即覆盖
2.4 close()方法其实内置了flush的方法功能

直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
当调用flush的时候，内容会真正写入文件
这样做是避免频繁的操作硬盘，导致效率下降(攒一堆，一次性写磁盘)
"""

# 打开文件，不存在的文件
open("C:/Log/3.txt", "w", encoding="UTF-8")
# .write 写入
f.write("hello word")  # 内容写到内存中
# flush 刷新
f.flush()  # 将内存中积攒的内容，写入到硬盘中
# close 关闭   其实内置了flush的方法，因此只需要调close就行
f.close()

# 3. 文件的追价操作 a模式
"""和w一样
a模式：当文件不存在，会创建文件；当文件存在，会继续在原内容后面继续写入
可以用”\n“写入换行符号
"""




