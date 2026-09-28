# day12.py —— 命令行通讯录（第 2 周的产出：能增删查）
#
# 今天的目标只有两个动作：① 加一个联系人  ② 按名字查出来
# 数据结构先想清楚：整张通讯录是一个【列表】，里面每个联系人是一条【字典】
#     contacts = [ {"name": "张三", "phone": "13800000000"}, ... ]
#
# 规则：三个 TODO 自己填，卡住了把报错贴给我，别自己硬扛

contacts = []   # 空通讯录，从零开始攒


def add_contact():
    """加一个联系人"""
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

    # TODO 1：把这个人存进 contacts
    #   第一步：先造一条记录（字典），装名字和电话
    #           record = {"name": ..., "phone": ...}
    #   第二步：把这条记录追加到列表里（列表的追加方法是哪个？D06 学过）
    #   第三步：打印一句"已添加 XXX"，好让你确认它真的进去了


def find_contact():
    """按名字查联系人"""
    key = input("请输入要查的名字：")
    for c in contacts:
        if c["name"] == key:
            print(f"找到了：{c['name']}   {c['phone']}")
            return
    print(f"通讯录里没有 {key}")

    # TODO 2：在 contacts 里找这个人
    #   思路：用 for 把 contacts 里的每条记录挨个拿出来，
    #        比较这条记录的 "name" 是不是等于 key
    #        找到了 → 打印姓名和电话，然后 return（找到就不必再往下找了）
    #        整个循环都走完还没找到 → 在循环外面打印"通讯录里没有 XXX"


def show_all():
    """看看现在都有谁（写代码时自查用，答辩也能演示）"""
    if len(contacts) == 0:
        print("通讯录还是空的")
        return
    for i, c in enumerate(contacts, 1):
        print(str(i) + ". " + c["name"] + "   " + c["phone"])


def main():
    while True:
        print()
        print("1 加联系人   2 查联系人   3 看全部   0 退出")
        choice = input("请选择：")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            find_contact()
        elif choice == "3":
            show_all()
        elif choice == "0":
            print("再见")
            break
        else:
            # TODO 3：提示"没有这个选项"
            #   注意：是"选项"，不是"科目"——D11 那次就写成"没有这个科目"了
            print("没有这个选项")
            continue


main()
