# day11.py —— JSON：把字典一键存成文件（D11）
# 日期：2026-09-21（D11）    时间：25 分钟
#
# ⭐ 今天学一个新东西：json 模块
#
# 【为什么学它】
#   昨天（D10）你是【手动】存文件的：
#       写：f.write(f"{k},{v}\n")       ← 自己定格式
#       读：k, v = line.split(",")      ← 自己拆格式
#   今天用 json，这两件事各变成【一行】：
#       写：json.dump(scores, f)        ← 自动
#       读：json.load(f)                ← 自动
#
#   ⭐ 而且 JSON 是【全世界通用的数据格式】——
#      微信、网页、App 之间传数据，用的都是它。
#
# 【怎么读这个文件】
#   白送你的：菜单框架（写过很多遍了，不重复劳动）
#   你写的：3 个 TODO
#   写完一个就用程序试一下


# ============================================================
# 知识卡：JSON 是什么
# ============================================================
#   JSON 就是一种【文本格式】，长得几乎和 Python 的字典/列表一模一样：
#
#       {
#         "数学": 85.0,
#         "英语": 76.0
#       }
#
#   ⭐ 关键：JSON 就是【字符串】，只不过这个字符串的写法有规矩。
#
#   ── 两个函数（就这两行最常用）──
#
#       json.dump(对象, 文件)    →  把字典/列表【写】进文件
#       json.load(文件)          →  从文件【读】回字典/列表
#
#   ── 两个参数（很重要）──
#
#       ensure_ascii=False   →  中文【原样显示】，不变成 \u6570\u5b66
#       indent=2             →  缩进 2 格，文件好看、易读
#
#   ⚠️ 三个必踩的坑：
#     ① 忘了 ensure_ascii=False  →  文件里全是 \uXXXX，看不懂
#     ② 忘了 import json         →  NameError: name 'json' is not defined
#     ③ json 只能存【基本类型】：字典/列表/字符串/数字/True/False/None
#        你的 scores 正好是 {字符串: 数字} → ✅ 能存
# ============================================================


import json          # ← 别忘这一行！

DATA_FILE = "scores.json"       # 数据文件名（和字典名区分开，避免看混）
scores = {}                     # 成绩字典


# ============================================================
# 白送你的：读文件（用 json！）
# ============================================================
import os

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        scores = json.load(f)               # ← 一行读出整个字典
    print(f"（已读回 {len(scores)} 条成绩）")


# ============================================================
# 白送你的：几个小函数（D08 学的 def）
# ============================================================
def show_all():
    """列出所有科目和分数"""
    if len(scores) == 0:
        print("  还没有成绩")
        return
    for i, (k, v) in enumerate(scores.items(), 1):
        print(f"  {i}. {k}：{v}")


def show_stats():
    """统计：平均分 / 最高分"""
    if len(scores) == 0:
        print("  还没有成绩")
        return
    avg = sum(scores.values()) / len(scores)
    best = max(scores, key=scores.get)
    print(f"  平均分：{avg:.2f}")
    print(f"  最高分：{scores[best]}（{best}）")


# ============================================================
# 白送你的：菜单主循环
# ============================================================
print("=== 成绩册 7.0（JSON 版）===\n")

while True:
    print("1. 录入成绩   2. 查看全部   3. 删除科目")
    print("4. 统计       5. 保存退出")
    choice = input("请选择：").strip()

    if choice == "1":
       k = input("输入科目数目：").strip()
       try:
            k = int(k)
       except ValueError:
            print("  不是整数，重来")
            continue
       for _ in range(k):
            line = input("  输入「科目 分数」：").strip()
            if line == "":
                break
            parts = line.split()
            if len(parts) != 2:
                print("  格式不对")
                continue
            try:
                scores[parts[0]] = float(parts[1])
                print(f"  已录入：{parts[0]}")
            except ValueError:
                print("  分数不是数字")

    elif choice == "2":
        show_all()

    elif choice == "3":
        print("删除哪一个科目:")
        want = input("  删除哪个科目：").strip()
        if want in scores:
            del scores[want]
            print("  已删除")
        else:
            print("  没有这个科目")

    elif choice == "4":
        show_stats()

    elif choice == "5":
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(scores, f, ensure_ascii=False, indent=2)
        print(f"  已保存 {len(scores)} 条到 {DATA_FILE}")
        break

    else:
        print("  没有这个选项")

    print()


# ============================================================
# 期望输出（第一次运行）
# ============================================================
#   === 成绩册 7.0（JSON 版）===
#
#   1. 录入成绩   2. 查看全部   3. 删除科目
#   4. 统计       5. 保存退出
#   请选择：1
#     输入「科目 分数」：数学 85
#     已录入：数学
#
#   请选择：1
#     输入「科目 分数」：英语 76
#     已录入：英语
#
#   请选择：4
#     平均分：80.50
#     最高分：85.0（数学）
#
#   请选择：5
#     已保存 2 条到 scores.json
#
# ── 存完之后打开 scores.json，你应该看到：──
#   {
#     "数学": 85.0,
#     "英语": 76.0
#   }
#
# ── 第二次运行（会先读回）──
#   （已读回 2 条成绩）
#   ...
#
#   ⭐ 对比一下 D10 存的 scores.txt：
#       D10 是「数学,85.0」一行一条（你自己定的格式）
#        D11 是 JSON 格式（全世界通用的格式）


# ============================================================
# 挑战题
# ============================================================
# 1. 对比实验：把 ensure_ascii=False 删掉，重新保存一次
#    打开 scores.json 看看变成什么样 → 就明白这个参数干嘛的了
#
# 2. 加一个功能：录入之前先判断"科目是否已存在"，
#    如果存在就问"要覆盖吗？"，输入 y 才覆盖
#
# 3. 想一想：为什么 json 能一行 store 整个字典，
#    而昨天要自己写循环？
#    （提示：JSON 的格式是【全世界统一的】，所以有现成的函数）
