"""
循环语句使用场景：
轮播图、音乐轮播、动态壁纸等等场景
"""
import random

# 1.while 循环语句
"""
while condition:
    条件满足时，做事情1
    条件满足时，做事情2
    条件满足时，做事情3
    只要条件满足，会无限循环执行

注意事项：
必须有条件 且条件会终止
"""
i = 0
while i < 100:
    print("小刘，继续努力")
    i += random.randint(1, 50)
print("努力成功了！")

# 案例：计算1+2+3+...+100
m = 1
sum = 0
while m <= 100:
    sum += m
    m += 1
print(f"1+2+3+...+100的和：{sum}")

# 案例：设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
""""numer = random.randint(1, 100)

not_finish = True
guess_count = 0
while not_finish:
    guess_number = int(input("请输入您猜测的数字："))
    guess_count += 1
    if numer == guess_number:
        print(f"恭喜您，猜中了,您总共猜了{guess_count}次")
        # 设置未False就是终止循环的条件
        not_finish = False
    elif numer > guess_number:
        print("猜小了")
    else:
        print("猜大了")
"""

# 2.while 嵌套循环语句
"""
while contion_1:
    条件满足要做的事情1
    while contion_2:
        条件满足1，且条件2满足要做的事情
"""

# 打印九九乘法表
# print不换行，需要加一个end = ''
print("打印", end="")
print("九九乘法表")
# 制表符tab的符号 就是 \t
print("hi\t刘浩宇")
print("hello\t张三")

# 控制行的循环1<=9
# 控制每一行的循环
p = 1
while p <= 9:
    # 定义内层循环的控制变量
    j = 1
    while j <= p:
        # 内层循环的print语句 不要换行
        print(f"{j} * {p} = {j * p}\t", end='')
        j += 1
    p += 1
    print()  # 空内容就是处于一个换行

# for循环 是一种轮询机制
"""
for 临时变量 in 待处理数据集：
    循环满足条件时执行的代码

注意：
无法定义循环条件，只能从被处理的数据集中，和java一样
"""

name = "birthday"
# 将name的内容，挨个取出赋予x临时变量
for x in name:
    print(x)

# 四、range() 使用
# [0-9]
for x in range(10):
    print(x)
# [3-9]
for y in range(3, 10):
    print(y)

# [3,5,7,9],步长为2
for z in range(3, 10,2):
    print(z)

# 五、break 和 continue
# break 终止循环
# continue 结束本次，开始下次






