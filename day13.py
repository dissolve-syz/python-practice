# day13.py —— 命令行通讯录（能【增】能【删】能【查】，今天开始能【记住】）
#
# 数据结构不变：整张通讯录是一个【列表】，每个联系人是一条【字典】
#     contacts = [ {"name": "张三", "phone": "13800000000"}, ... ]
#
# 9/25（D15）加的目标只有一个：
#     【关掉程序再打开，人还在】—— 也就是把通讯录存进文件、下次启动读回来。
#     你在 D11 已经对成绩册做过一模一样的事（json.dump / json.load），这里是换一份数据再做一遍。
#
# 今天只加两个函数 + 两处调用，别的代码一个字都别改。

import json                      # 今天要用到它（D11 学过）

DATA_FILE = "contacts.json"      # 存放通讯录的文件名

contacts = []


def add_contact():
    """加一个联系人（已完成，别动）"""
    while True:
        parts = input("请输入姓名和电话（中间空格）：").strip()
        if parts == "":
            return

        part = parts.split()
        if len(part) != 2:
            print("格式不对，要写成「姓名 电话」")
            continue
        name = part[0]
        phone = part[1]
        try:
            int(part[1])
        except ValueError:
            print("电话不是数字，重来")
            continue
        record = {"name": name, "phone": phone}
        contacts.append(record)
        print(f"已添加 {name}")


def find_contact():
    """按名字查联系人（已完成，别动）"""
    key = input("请输入要查的名字/电话：").split()
    for c in contacts:
        if c["name"] == key or c["phone"] == key:
            print(f"找到了：{c['name']}   {c['phone']}")
            return
    print(f"通讯录里没有 {key}")


def show_all():
    """看全部（已完成，别动）"""
    if len(contacts) == 0:
        print("通讯录还是空的")
        return
    for i, c in enumerate(contacts, 1):
        print(str(i) + ". " + c["name"] + "   " + c["phone"])


def del_contact():
    """按名字删掉一个联系人（D13 已完成，别动）"""
    key = input("请输入要删除的名字：").split()
    for i, c in enumerate(contacts):
        if c["name"] == key:
            del contacts[i]
            print(f"已删除 {key}")
            show_all()
            return
    print(f"通讯录里没有 {key}")


def save_data():
    """把 contacts 存进 contacts.json        ← 今天要写的第 1 个函数"""
  
    with open (DATA_FILE,"w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
    print(f"已保存 {len(contacts)} 位联系人")
    # ================== TODO 1：存盘 ==================
    # D11 你在成绩册上写过一模一样的：
    #     with open(文件名, "w", encoding="utf-8") as f:
    #         json.dump(数据, f, ensure_ascii=False, indent=2)
    #
    # 三处填一填：
    #   ① 文件名用上面那个 DATA_FILE
    #   ② 要存的"数据"就是 contacts 这个列表
    #   ③ ensure_ascii=False 必须写！不然中文会存成 \u4e2d\u6587 那种乱码
    #
    # 存完在函数最后打印一句「已保存 N 位联系人」，N 自己想办法取（len 会用吧）
    # ==================================================


def load_data():
    """启动时把 contacts.json 读回来        ← 今天要写的第 2 个函数"""
    import os
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            contacts[:] = json.load(f)
        print(f"已载入 {len(contacts)} 位联系人")
    else:
        print("还没有存档，从空的开始")

     
    # ================== TODO 2：读盘 ==================
    # 这里比存盘多一个坑：**第一次运行时文件根本不存在**，直接 open 会崩。
    # D10 你学过 os.path.exists()，先判断一下文件在不在：
    #     在  → 打开、json.load() 读回来，装进 contacts
    #     不在 → 什么都不做（contacts 本来就是空的），也可以打印一句「还没有存档，从空的开始」
    #
    # 注意一个大坑：**要把读回来的内容塞进那个全局的 contacts**，
    # 不能写成 contacts = ...（那样会造一个新的局部变量，外面的 contacts 还是空的）
    # 正确写法是原地改：contacts.extend(读回来的东西)  或者  contacts[:] = 读回来的东西
    #
    # 读回来装好后，打印一句「已载入 N 位联系人」，让你一眼看到它记住了几个人
    # ==================================================


def main():
    load_data()          # ← TODO 3 之一：启动就先读一次（把上面写好的函数叫过来）

    while True:
        print()
        print("1 加联系人   2 查联系人   3 看全部   4 删联系人   0 退出")
        choice = input("请选择：")

        if choice == "1":
            add_contact()
        elif choice == "2":
            find_contact()
        elif choice == "3":
            show_all()
        elif choice == "4":
            del_contact()
        elif choice == "0":
            save_data()      # ← TODO 3 之二：退出前存一次（不然白加）
            print("再见")
            break
        else:
            print("没有这个选项")


main()
