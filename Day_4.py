#黑马课程Day2：if/eilf/else判断；while和for循环的基础用法；以及range语法
#if语句登录判断
login_name = input("请输入的你账号: ")
password = input("请输入的你密码: ")
if login_name == "zyq" and password == "202610":
    print(f"账号：{login_name}，密码：{password};校验成功！")
# elif login_name != "zyq":
#     print(f"账号:{login_name}错误，不是“zyq”，校验失败！")
# else:
#     print(f"密码:{password}错误，不是“202610”，校验失败！")
else:
    print(f"账号或密码错误，校验失败！")

#联系案例：需求:根据用户输入的年份，判断这一年是闰年还是平年。
# 非整百年份，且能被4整除的年份是闰年；整百年份(如1900年、2000年)必须能被400整除才是闰年
year = int(input("请输入查询的年份"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}年份是闰年！")
else:
    print(f"{year}年份不是闰年！")

# 需求1:根据用户输入的数字，判断该数字是奇数还是偶数。
number = int(input("请输入查询的数字："))
if number % 2 == 0:
    print(f"{number}是偶数！")
else:
    print(f"{number}是奇数！")

# 需求2:根据用户输入的年龄，判断该用户是否已经成年(>=18，成年;否则，未成年)。
age = int(input("请输入查询的年龄："))
if age >= 18:
    print(f"{age}岁，已成年！")
else:
    print(f"{age}岁，未成年！")

# 需求3:根据用户输入的数字，判断该数字是正数还是负数(不考虑0)。
number_2 = float(input("请输入查询的数字："))
if number_2 == 0:
    print(f"{number_2}既不是正数，也不是负数")
elif number_2 > 0:
    print(f"{number_2}是正数！")
else:
    print(f"{number_2}是负数！")

# 三角形类型判断:根据输入的三个边的边长(正整数)，判定是等边三角形、等腰三角形、普通三角 形，还是不能构成三角形。
# 构成三角形的条件:两边之和大于第三边
a=int(input("请输入边长a："))
b=int(input("请输入边长b："))
c=int(input("请输入边长c："))
if a+b>c and a+c>b and b+c>a:
    #  三个边都相等:等边三角形
    if a == b == c:
        print(f"边长{a, b, c}组成等边三角形")
    # ·两个边相等:等腰三角形
    elif a == b or b == c or a == c:
        print(f"边长{a, b, c}组成等腰三角形")
    #  三个边都不相等:普通三角形
    else:
        print(f"边长{a, b, c}组成普通三角形")
else:
    print(f"边长{a, b, c}不满足两边之和大于第三边！无法组成三角形")

#while循环：案例：循环输出10次：我是python初学者
#while循环中else可有可无，若退出循环时需要做事情，则添加else处理
c = 0
while c < 10:
    c = c + 1
    print(f"第{c}次循环输出：我是python初学者！！")
else:
    print(f"已完成{c}次输出，退出循环")
#使用for循环：
for i in range(10):
    i = i + 1
    print(f"第{i}次循环输出：我是python初学者！！")

#计算1-100所有偶数和
number_3 = 1
sum_num = 0
while number_3 <= 100:
    if number_3 % 2 == 0:
        sum_num += number_3
    number_3 += 1
print(f"1-100所有偶数和为{sum_num}")

# 使用for循环：
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(f"1-100所有偶数和为{total}")

# while循环是通过条件表达式来控制是否要进行下一次循环的。而for循环，本质是一种轮询遍历机制，对一批内容进行逐个处理。
# for循环与while循环的场景：
# while循环:用于在某个条件满足时一直循环，循环的次数通常是未知的，只知道循环开始/结束的条件。(关注的是循环的条件)
# for循环:用于对一个已知的数据集进行遍历或已知次数的循环。(关注的是遍历每一个元素)

# 案例：计算100-500之间所有3的倍数的数字之和。
#使用while循环
number_4 = 100
total_num = 0
while number_4 <= 500:
    if number_4 % 3 == 0:
        total_num += number_4
    number_4 += 1
print(f"100-500之间所有3的倍数的数字之和为{total_num}")

# 使用for循环：
total_num_for = 0
for f in range(100, 500):
    if f % 3 == 0:
        total_num_for += f
print(f"100-500之间所有3的倍数的数字之和为{total_num_for}")

# range语句 作用:生成指定规则的数字序列
# 用法1:range(end)->获取一个从@开始，到end结束的数字序列(不含end本身)
# range(5)获取的数据就是0,1,2,3,4

# 用法2:range(start,end)->获取一个从start开始，到end结束的数字序列(不含end本身)
# range(2,8)获取的数据就是 2,3,4,5,6,7

# 用法3:range(start,end,step)->获取一个从start开始，到end结束的数字序列,step步长(不含end本身)
# range(0,10,2)获取的数据就是0,2,4,6,8
for r in range(1,10,4):
    print(r)