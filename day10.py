# day10.py —— 文件读写：让程序"记住"东西（D10）
# 日期：2026-09-19（D10）    时间：25 分钟
#
# ⭐ 今天学一个新东西：文件读写
#
# 【为什么要学】
#   你前面 9 天写的程序，一关掉数据就没了。
#   学了文件读写，程序就能把数据存到硬盘上，下次打开还在 ——
#   这才叫"真的能做工具"。
#
# 【和你会的 C 语言对照】
#   C:      FILE *f = fopen("a.txt", "w");  fprintf(f, ...);  fclose(f);
#   Python: with open("a.txt", "w", encoding="utf-8") as f:
#               f.write(...)
#   思路一样（打开→读写→关闭），但 Python 不用管指针，而且 with 会自动关。
#
# 【怎么读这个文件】
#   白送你的：输入框架
#   你写的：3 个 TODO
#   写完一个就把对应的 print 注释去掉


# ============================================================
# 知识卡
# ============================================================
#   打开文件：
#       f = open("scores.txt", "w", encoding="utf-8")
#       ...
#       f.close()                    ← 必须自己关
#
#   更好的写法（自动关，推荐）：
#       with open("scores.txt", "w", encoding="utf-8") as f:
#           f.write("内容")
#
#   ── 三个模式 ──
#       "w"  写（【会清空】原内容！）
#       "a"  追加（在末尾加）
#       "r"  读
#
#   ── 常用方法 ──
#       f.write("字符串")     ← ⚠️ 只能写字符串！数字要先 str() 转
#       f.read()              ← 读全部，返回一个字符串
#       for line in f:        ← 一行一行读（最常用）
#
#   ⚠️ 三个必踩的坑：
#     ① 一定要写 encoding="utf-8"！
#        不写的话，Windows 上中文会乱码或者直接报错
#     ② f.write() 只能写字符串
#        f.write(85)      → 报错
#        f.write(str(85)) → 对
#     ③ "w" 模式会【清空】文件
#        想追加要用 "a"
# ============================================================


FILENAME = "scores.txt"        # 存到程序同一个文件夹下

scores = {}

print("=== 成绩册 6.0（能存盘的版本）===")
print("输入格式：科目 分数  （中间空格）")
print("直接回车结束\n")
import os
if os.path.exists(FILENAME):
     with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                k, v = line.split(",")
                scores[k] = float(v)
                print(f"{scores[k]}")

# ---------- TODO 1：启动时先把上次存的读回来 ----------
# 要求：
#   如果 scores.txt 存在 → 读进来，填进 scores 字典
#   如果不存在 → 什么都不做（第一次运行时肯定没有，不能崩）
#
# 提示：
#   import os
#   if os.path.exists(FILENAME):        ← 先判断文件在不在
#       with open(FILENAME, "r", encoding="utf-8") as f:
#           for line in f:
#               line = line.strip()      ← 去掉行尾的换行符
#               if line == "":
#                   continue
#               k, v = line.split(",")   ← 用逗号切开，复习 D09 的 split
#               scores[k] = float(v)
#
# ⚠️ 这段要写在【输入循环之前】，否则每次都被清空


# 写完把下面这段注释去掉：
if scores:
    print(f"（已从文件读回 {len(scores)} 条成绩）")
    print()


while True:
    line = input("输入：").strip()
    if line == "":
        break

    parts = line.split()

    if len(parts) != 2:
        print("格式不对，要写成「科目 分数」")
        continue

    subject = parts[0]
    try:
        score = float(parts[1])
    except ValueError:
        print("分数不是数字，重来")
        continue

    scores[subject] = score
with open(FILENAME, "w", encoding="utf-8") as f:
    for k, v in scores.items():
        f.write(f"{k},{v}\n")
with open(FILENAME, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"第{i}行: {line.strip()}")

# ---------- TODO 2：把所有成绩存进文件 ----------
# 要求：
#   把 scores 里的每一条，写成一行 `科目,分数`
#   存完之后打印"已保存 N 条"
#
# 提示：
#   with open(FILENAME, "w", encoding="utf-8") as f:
#       for k, v in scores.items():
#           f.write(f"{k},{v}\n")       ← 别忘最后的 \n（换行）
#
# ⚠️ "w" 模式会清空原文件 —— 这正是我们想要的（每次都全量重写）


# 写完把下面这行注释去掉：
print(f"已保存 {len(scores)} 条到 {FILENAME}")


# ---------- TODO 3：把存进去的东西再显示出来验证 ----------
# 要求：
#   读回文件，逐行打印，证明真的存进去了
#   格式：`第1行: 数学,85.0`
#
# 提示：
#   with open(FILENAME, "r", encoding="utf-8") as f:
#       for i, line in enumerate(f, 1):      ← 复习 D06 的 enumerate
#           print(f"第{i}行: {line.strip()}")


# 写完把下面这行注释去掉：
print(f"\n=== {FILENAME} 里的内容 ===")


# ============================================================
# 期望输出（第一次运行：输入 数学 85 / 英语 76，然后回车）
# ============================================================
#   === 成绩册 6.0（能存盘的版本）===
#   输入格式：科目 分数  （中间空格）
#   直接回车结束
#
#   输入：数学 85
#   输入：英语 76
#   输入：
#   已保存 2 条到 scores.txt
#
#   === scores.txt 里的内容 ===
#   第1行: 数学,85.0
#   第2行: 英语,76.0
#
# ── 第二次运行（直接回车，不输入任何东西）──
#   === 成绩册 6.0（能存盘的版本）===
#   ...
#   （已从文件读回 2 条成绩）
#   已保存 2 条到 scores.txt
#   ...
#
#   ⭐ 第二次运行能读回上次的数据 —— 那就成功了


# ============================================================
# 挑战题（做完了再碰）
# ============================================================
# 1. 把成绩按分数从高到低【排序后】存进文件
#    提示：D07 学过 sorted()，D09 的挑战题也提过 sorted(d.items(), key=...)
#
# 2. 加一个功能：输入 "del 数学" 能把某个科目删掉
#    提示：D09 知识卡里有 del
#
# 3. 想一想：为什么第一次运行读不到东西？
#    （提示：文件还不存在）
