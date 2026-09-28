# debug_day4.py —— 带调试输出的版本
# 目的：查清楚"输入 q 为什么没退出"
#
# 用法：用这个文件跑一遍，输入 q，然后把屏幕上出现的【所有内容】复制发给我


round_num = 0

while True:
    round_num += 1
    print(f"========== 第 {round_num} 轮开始 ==========")

    s = input("请输入成绩（输入 q 退出）：")

    # ↓↓↓ 这几行是这次加的"显微镜"，把收到的输入原形毕露地打出来
    print(f"[调试] 你输入的是      : {s!r}")
    print(f"[调试] 它的长度        : {len(s)}")
    print(f"[调试] 它等于 'q' 吗   : {s == 'q'}")
    if len(s) > 0:
        print(f"[调试] 第一个字符的编码 : {ord(s[0])}  （半角 q 应该是 113）")

    if s == "q":
        print("[调试] ★ 命中 break！循环应该结束了")
        break

    try:
        score = int(s)
    except ValueError:
        print("[调试] 转换失败 -> 走 except -> continue 回到循环开头")
        continue

    if score >= 90:
        print("成绩等级：A")
    elif score >= 80:
        print("成绩等级：B")
    elif score >= 70:
        print("成绩等级：C")
    elif score >= 60:
        print("成绩等级：D")
    else:
        print("成绩等级：F")

print("[调试] 循环已结束，程序正常退出")
