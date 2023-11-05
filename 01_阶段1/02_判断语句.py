# 一、数字子类型的另一个子类 布尔（bool）
# 布尔类型的定义 True 和 False
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容：{bool_1},bool_2变量的内容：{bool_2}")

# 比较运算符 == != > < >= <=
print(f"3>2的结果：{3 > 2}")
# 二、if语句
""" 注意依靠缩进来判断代码块是不是属于该if语句
if 要判断条件：
    条件成立时，要做的事情
"""
# 定义变量
mct_time = 90
input_time = input("请输入一个整数时间点：")
if int(input_time) >= mct_time:
    print(f"您输入的时间是{input_time},大于{mct_time},可以拼接")
print("这块不属于if语句了----")

# 三、if else 语句
"""
if 条件：
    满足需要做的事情2
    满足需要做的事情2
    ...
else:
    不满足需要做的事情1
    不满足需要做的事情2
    ...
"""
age = input("请输入您的年龄：")
if int(age) >= 18:
    print(f"您已经成年，需要买票10元")
else:
    print("您未成年，可以免费游玩")
print("祝您游玩愉快！")

# 四、if elif else语句的使用
"""
if 条件1:
    条件1满足应该做的事情
elif 条件2:
    条件2满足应该做的事情
elif 条件3:
    条件3满足应该做的事情
else:
    条件都不满足应该做的事情
"""
if int(input("请输入身高：")) < 120:
    print("身高小于120cm，可以免费")
elif int(input("请输入vip级别(1-5)：")) >= 3:
    print("vip级别大于等于3，可以免费")
else:
    print("不可以免费")

# 五、if语句的嵌套判断
"""
if contion_1:
    满足条件1 做的事情1
    if 条件2：
        满足条件2 做的事情1
"""
print("欢迎进入去哪儿网客户端！")
number = int(input("输入您的Qt账号："))
if number > 100:
    print("您是普通员工！")
    if number > 200:
        print("您是2023年的新员工")
    else:
        print("您是2022年入职的员工")
else:
    print("您是老员工")
print("新的一天，祝您工作愉快！")

# 猜测数字案例
# 1.构建一个随机数
import random

number = random.randint(1, 10)

guess_num = int(input("输入你要猜测的数字："))

# 2 通过if判断进行数字的猜测
if guess_num == number:
    print("恭喜你，第一次就猜中了")
else:
    if guess_num > number:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")

    guess_num = int(input("再次输入你要猜测的数字："))
    if guess_num == number:
        print("恭喜你，第一次就猜中了")
    else:
        if guess_num > number:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")
        guess_num = int(input("第三次输入你要猜测的数字："))
        if guess_num == number:
            print("恭喜你，第一次就猜中了")
        else:
            if guess_num > number:
                print("你猜测的数字大了")
            else:
                print("你猜测的数字小了")
        print("三次猜测机会用完了！答案是：", number)
