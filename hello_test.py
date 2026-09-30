# 我的第一个测试脚本：模拟 bug 数据统计
bugs = ["登录超时", "金额显示错误", "按钮错位", "支付失败", "订单重复"]

severity = {"高": 0, "低": 0}
for bug in bugs:
    if "金额" in bug or "支付" in bug or "订单" in bug:
        severity["高"] += 1
    else:
        severity["低"] += 1

print("本周 bug 总数:", len(bugs))
print("严重 bug:", severity["高"], "个 -->", [b for b in bugs if severity])
print("处理完成，通知开发修改！")