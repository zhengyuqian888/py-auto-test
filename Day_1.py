# 第一天练习学习python脚本，实操敲代码
from itertools import count

module_name:str = "订单模块"              #模块名称-str字符串类型
case_total:int = 36                     #用例总数-int整数类型
pass_rate:float = 95.8               #通过率-float小数类型

print("测试",module_name,"时，共",case_total,"条用例，通过率",pass_rate,"%")

#虽然可以用print直接输出结果；但后续代码或输出报告时，若想使用该结果，还是需要使用report拼接变量，方便直接调用
report=f"测试{module_name}时,共{case_total}条用例，通过率{pass_rate}%"
print(report)

#金额、小数高频敏感问题实践,float小数相加0.1+0.2不等于0.3，等于0.300000000000004
print("0.1+0.2=",0.1+0.2)

failed_case:int = 6                      #定义用例失败数量，尝试一下使用加减程序计算方法输出结果
report_again=(f"测试{module_name}时，共{case_total}条用例，通过率{(case_total-failed_case)/case_total*100:.2f}%，"
              f"bug几率{failed_case/case_total*100:.2f}%")
print(report_again)

#尝试制定用例dict键值对，创建第一条测试用例
case = {
    "id":"cs000",
    "login_name":"zyq",
    "password":"20261001",
    "code":"9999"}
case["title"] = "第一个用例是测试登录"         #用例新增一个title字段

print("用例编号：",case["id"],"\n用例标题：",case["title"])

#在创建一个测试用例
# demo = {
#     "order":"",
#     "prices":"",
#     "good_name":"",
#     "num":"",
#     "good_price":"",
#     "desc":""
# }

#创建多条用例列表
cases=[
    case,
    {"id":"cs001","login_name":"zyq","password":"20261001","code":"8888"},
    {"id":"cs002","login_name":"中文名称","password":"中文密码","code":"7777"},
    {"id":"cs003","login_name":"超长的中文名称（略）","password":"english","code":"6666"},
    {"id":"cs004","login_name":"zyq2026","password":"2026","code":"y8dR56"},
    {"id":"cs005","login_name":"zyq%$@^*","password":"","code":"Cstt"},
    {"id":"cs006","login_name":"","password":"334761","code":"Cstt"},
    {"id":"cs007","login_name":"zyq","password":"334761","code":""},
    # 同一个list中语法可以存在多个键值对方式的dict，但for循环遍历时会报错，所以一个list中最好只放一种dict
    # demo,
    # {"order":"e87fyuf55e9d7df","prices":"88.88","good_name":"凤梨","num":"2","good_price":"44.44","desc":""},
    # {"order":"s8d7f8sjods9df8","prices":"66.32","good_name":"西瓜","num":"1","good_price":"33.16","desc":""},
    # {"order":"usoufs8d78677s7","prices":"40.8","good_name":"猕猴桃","num":"22","good_price":"20.4","desc":""}
]

matched = []                                             #创建一个空列表，用以后续存放循环统计的数据
matched_like = []
for c in cases:                                          #c也只是一个自定义的循环变量名，可随意取
    if c["login_name"]=="zyq":                           #==精准匹配zyq
        matched.append(c["id"])        #将遍历匹配成功的记录id放进matched列表中
    if "zyq" in c["login_name"]:                         #遍历模糊匹配login_name含有“zyq”的数据
        matched_like.append((c["id"],c["login_name"]))   #将匹配成功的记录id和login_name字段值放进matched_like列表中

#len即为length，获取列表长度，len(cases)即为统计列表有多少条数据，len（case）即为统计用例有多少字段
# （注意后面单独新增的title字段也要统计进去）
print("共",len(cases),"条用例，case用例有",len(case),"个字段，其中："
"\ncase用例中，登录名称是“zyq”的有",len(matched),"条记录，分别是",matched,
"\n包含“zyq”的登录名称有",len(matched_like),"条记录，分别是",matched_like,
      )
print("第一条用例是",cases[0],"\n第二条用例是",cases[1],"\n最后一条用例是",cases[-1])

last_report = f"cases列表共有{len(cases)}条用例，其中login_name包含“zyq”的用例有{len(matched_like)}条"
print(last_report)