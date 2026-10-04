#第2天，昨日回顾，for循环学习、批量生成测试数据 + 冒烟结果判定
import random

bugs = ["","登录密码错误","登录502报错","支付跳转异常","","支付金额错误","页面UI显示错乱","订单状态未更新","提示文案优化"]

critical_bug = []                  #严重bug列表
minor_bug = []                     #轻微bug列表
high_bug = []
high_bug_merge = []
empty_count: int = 0
kewords = ["报错","错乱","错误","支付"]             #制定关键词匹配列表，方便调用并维护关键词
all_kewords = ["提示","优化"]

    # 关键词调用匹配,any是满足任意一个条件的意思，可以理解为bug列表和kewords任意一个关键词匹配即可
    # elif "报错" in bug or "错乱" in bug or "错误" in bug or "支付" in bug:这种旧写法不利于后续调用维护
    # elif = else if 的缩写，意思是"否则再看看下一个条件"。它不能单独用，必须跟在一个 if 后面，形成一个"多选一"的链条
    # 顺序很重要：越苛刻、优先级越高的条件要放前面。链条从上往下判断，命中一个就跳出，后面的条件不再判断——所以条件之间不会互相"漏"
    # 比如"支付+金额"必须先判，如果if "支付" in bug and "金额" in bug条件，
    # 放在elif any(k in bug for k in kewords)关键词匹配下方，就会直接被截胡，无法获取到准确数据

for bug in bugs:
    if bug == "":
        #在同一层循环中，任意操作需要在continue上方，否则直接跳过不执行了
        empty_count += 1
        continue
    #我需要bug列表中的某一项数据可以满足多个if条件的筛选，但又不互相影响
    #所以定义布尔值Boolean，类似于昨日report拼接调用，方便更改规则，以实现打破if、elif、else的互斥
    #因匹配“bug”变量，所以需要在循环内创建，否则无法识别“bug”是什么
    boo_high = any(k in bug for k in kewords)               #成功匹配（满足）kewords列表任意一个条件即可
    boo_high_merge = all(k in bug for k in all_kewords)     #成功匹配（满足）all_kewords列表所有条件
    if "支付" in bug and "异常" in bug:
        high_bug.append(bug)
    if boo_high:
        critical_bug.append(bug)
        # print("严重bug有", len(critical_bug), "个,分别是：", critical_bug)
        # 不能将print放到for循环里面，否则每遍历一次就要打印一次
    if boo_high_merge:
        high_bug_merge.append(bug)
    if not boo_high and not boo_high_merge:
        minor_bug.append(bug)
print("严重bug有",len(critical_bug),"个,分别是：",critical_bug)
print("轻微bug有",len(minor_bug),"个,分别是：",minor_bug)
print("all函数写法bug：",len(high_bug_merge),"个,具体是",high_bug_merge,
      ";另外，注意bug列表中还有",empty_count,"个空值；以及支付跳转问题的",len(high_bug),"个bug：",high_bug)

#练习随机数等函数生成手机号
phones = []
for phone in range(6):                                        #随机6次
    prefix = random.choice(["182","183","159","138","139"])   #prefix前缀，在列表中随机选择
    # suffix后缀，自动随机填充1111~99999999正整数,zfill(8)是指不满8位数的随机数时，自动补位0，
    # 例如随机数是88888，那么自动填充为00088888（左侧补位），zfill是字符串类型，所以是str
    # suffix = str(random.randint(1111,99999999)).zfill(8)
    # 同理写法“:08d”，不满8位数的随机数时，左侧自动补位0
    # suffix = f"{random.randint(1111,9999):08d}"
    # 任意字符写法“:*>8”，不满8位数的随机数时，左侧自动补位*,*可以改为任意字符，汉字、数字、英文、符号均可，但只能是一个字符
    # 若是“:*<8”，则代表不满8位数的随机数时，右侧自动补位*
    suffix = f"{random.randint(1111,9999):*>8}"
    phones.append(prefix+suffix)
print(f"共生成了{len(phones)}个手机号，分别为{phones}")