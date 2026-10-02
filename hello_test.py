# 我的第一个测试脚本：模拟 bug 数据统计
bugs = ["登录超时", "金额显示错误", "按钮错位", "支付失败", "订单重复"]

severity = {"严重": 0, "一般": 0}
high_bug_list = []#存放“严重”级别bug
low_bug_list = []#存放“一般”级别bug
for bug in bugs:
    if "金额" in bug or "支付" in bug or "订单" in bug:
        severity["严重"] += 1
        high_bug_list.append(bug)
    else:
        severity["一般"] += 1
        low_bug_list.append(bug)

#__name__ 是 Python 内置变量：
# 直接运行本文件时，__name__ 等于 "__main__"，条件成立，打印会执行
# 被其他文件 import 时，__name__ 等于模块名 "hello_test"，条件不成立，打印被跳过
if __name__ == "__main__":
    print("本周 bug 总数:", len(bugs))
    print("严重级别 bug:", severity["严重"], "个 -->",high_bug_list,
          "\n一般级别 bug:", severity["一般"], "个 -->",low_bug_list)
    print("统计完成，通知开发修改！")