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

print("本周 bug 总数:", len(bugs))
print("严重级别 bug:", severity["严重"], "个 -->",high_bug_list,
      "\n一般级别 bug:", severity["一般"], "个 -->",low_bug_list)
# print("一般级别 bug:", severity["一般"], "个 -->",low_bug_list)
print("统计完成，通知开发修改！")