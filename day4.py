# day4.py —— 第四天：循环 while / for
# 运行方式：点右上角 ▶ ，或者终端里敲 python day4.py
#
# 今天的产出：把前三天的「成绩等级判断」升级成一个【真正能用】的程序
#   —— 可以反复输入成绩，输入一次算一次，输 q 退出


# ========== 先看这个：C 的 for 和 Python 的 for 完全不是一回事 ==========
#
#   C 的 for 是"三段式计数器"：
#       for (int i = 0; i < 5; i++) {
#           printf("%d\n", i);
#       }
#
#   Python 的 for 是"遍历序列"（for-each），不是计数器：
#       for i in range(5):
#           print(i)
#
#   记住这一句就够了：
#       【C 的 for  ≈  Python 的 while】
#       【Python 的 for 是"把一堆东西挨个拿出来"】
#
#   还有两个 C 习惯必须改掉：
#     1. Python 里【没有 i++、i--】！只能写 i += 1
#     2. 冒号和缩进的老规矩不变


# ---------- 第 1 步：while 计数（约 5 分钟）----------
# TODO: 用 while 打印 0 到 4：
#
#     i = 0
#     while i < 5:
#         print(i)
#         i += 1        ← 这行千万别忘！忘了就是死循环
#
#   ⚠️ 死循环急救：程序卡住不动或一直刷屏，在终端里按 Ctrl + C 强制停


# ---------- 第 2 步：for + range（约 5 分钟）----------
# TODO: 用 for 打印 0 到 4，感受一下和 while 的区别：
#
#     for i in range(5):
#         print(i)
#
#   然后自己试着回答（改代码验证，别猜）：
#     range(1, 6)     打印什么？
#     range(0, 10, 2) 打印什么？
#     range(5, 0, -1) 打印什么？


# ---------- 第 3 步：break 和 continue（约 5 分钟）----------
#     break    = 立刻跳出整个循环，后面的都不做了
#     continue = 跳过本轮剩下的代码，直接开始下一轮
#
# TODO: 写一个 for i in range(10)，当 i == 5 时 break，
#       看看到几就停了。然后把 break 改成 continue，对比区别。


# ---------- 第 4 步：今天的重头戏（约 15 分钟）----------
# 把前三天学的全部串起来，做一个真正能用的程序：
#
#   1. 用 while True 做无限循环（True 恒为真，所以会一直转）
#   2. 每次问用户输入成绩
#   3. 输入 q 就 break 退出
#   4. 用 try/except 接住"输入的不是数字"的情况
#   5. 用 if/elif/else 判断等级并打印
#
# TODO: 自己写出来，形状是：
#
#     while True:
#         s = input("请输入成绩（输入 q 退出）：")
#         if s == "q":
#             break
#         try:
#             score = int(s)
#         except ValueError:
#             print("输入的不是数字，请重新输入")
#             continue
#         # ↓ 这里写你的 if / elif / else 判断等级
#
#   ⚠️ 想一个问题：为什么 continue 必须写在 except 块【里面】，
#      写在 try/except 外面不行？


# ---------- 选做（约 10 分钟）----------
# TODO: 加一个统计功能：退出时告诉用户"你一共算了 N 次成绩"
#       提示：在循环【外面】定义 count = 0，每成功算一次就 count += 1，
#             循环结束后再打印它
#
#       想一想：为什么 count = 0 必须写在循环外面？
#       如果写在 while True 里面会发生什么？


# ---------- 卡住了怎么办 ----------
#   程序不动了 / 一直刷屏   → Ctrl + C 强制停止
#   SyntaxError            → 九成是冒号或缩进
#   TypeError              → 类型不对
#   能跑但结果不对          → 在循环里加 print(变量) 把中间过程打出来看
#
#   还是不行就把报错整段发给助手。今天这题有点长，超过 10 分钟没进展就问。

#while i<5:
   # print(i)
    #i+=1
#for i in range(0,10,1):
   # if i==5:
       # continue
   # print(i)   
while True:
    s = input("请输入成绩（输入 q 退出）：")
    if s == "q":
        break
    try:
        score = int(s)
    except ValueError:
        print("输入的不是数字，请重新输入")
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
    


