# Python 速查（学到哪记到哪）

> 位置：`D:\python\00-Python速查.md`
> 用途：忘了语法就翻这里，不用问会话。
> 从 D06（2026-09-15）开始记。

---

## 一、列表（list）

```python
scores = []                  # 建一个空列表
scores = [85, 92, 60]        # 直接建一个有三个数的列表

scores.append(88)            # 往末尾追加一个
len(scores)                  # 里面有几个
scores[0]                    # 第 1 个  ← 索引从 0 开始！
scores[1]                    # 第 2 个
scores[-1]                   # 最后一个
sum(scores)                  # 求和
max(scores) / min(scores)    # 最大 / 最小
```

**列表解决的核心问题：不用猜初始值。**

```python
# ❌ 累加器写法：要自己维护"还没有数的时候是什么"
total = 0
maxss = 0          # ← 猜错了！数据里有负数或 0 到 1 之间的小数就错
for s in scores:
    ...

# ✅ 列表写法：不用猜
total = sum(scores)
maxss = max(scores)
```

---

## 二、for 循环：Python 和 C 不一样 ⚠️

### C 的 for 给你「下标」

```c
for (int i = 0; i < n; i++) {
    printf("%d", arr[i]);     // 自己维护 i，再用 arr[i] 取
}
```

### Python 的 for 直接给你「元素」

```python
for sc in scores:             # 对于 scores 里的每一个 sc
    print(sc)                 # 没有 i，没有 scores[i]
```

| | C | Python |
| --- | --- | --- |
| 给你什么 | 下标 `i` | **元素本身** |
| 取元素 | `arr[i]` | 直接用 `sc` |
| 何时结束 | 你写 `i < n` | **自动判断** |
| 越界风险 | 有（`i <= n` 就崩） | **没有** |

**`sc` 是随便起的名，不用提前定义，每次循环自动换成下一个元素。**

```python
for sc in scores:       # 都行
for x in scores:
for score in scores:
```

### 需要下标的时候

```python
for i in range(len(scores)):      # C 风格，能用但不 Python
    print(scores[i])

for i, sc in enumerate(scores):   # ✅ 同时给序号和元素
    print(i, sc)
```

**`enumerate` 干的事**：给每个元素配一个序号，变成一串配对。

```python
scores = [100, 59, 85]

enumerate(scores)  →   (0, 100)
                       (1,  59)
                       (2,  85)
                        ↑    ↑
                      序号   元素
```

```python
for i, sc in enumerate(scores):
    print(f"第 {i+1} 个：{sc}")     # i 从 0 开始，所以「第几个」要 +1
```

---

## 三、元组解包 ⭐（交换 / enumerate 都是它）

**Python 里一大类写法都靠这一个机制。吃透它，很多"看不懂"的代码就通了。**

### 规则：右边先全部算完 → 打包成一个整体 → 再拆开赋给左边

### 用一：交换两个值

```python
scores[i], scores[j] = scores[j], scores[i]
```

**为什么不能直接换**：

```python
scores[i] = scores[j]     # scores[i] 被覆盖，原值丢了
scores[j] = scores[i]     # 两个都成同一个值
```

**C 需要临时变量**：`temp = a; a = b; b = temp;`

**Python 不用**，因为执行分两步：

```
① 右边先算完     →   (85, 59)        ← 两个值都取出来了，打包
② 再拆开赋值     →   scores[i]=85, scores[j]=59
```

右边全部算完之后才开始赋值，所以原值不会被中途覆盖。

### 用二：同时赋多个值

```python
a, b, c = 1, 2, 3
x, y = y, x
```

### 用三：接住 enumerate 的配对

```python
for i, sc in enumerate(scores):     # 每轮拆一个 (序号, 元素)
    ...
```

### 用四：函数返回多个值

```python
def minmax(nums):
    return min(nums), max(nums)     # 返回的是一个元组

lo, hi = minmax([3, 1, 5])          # 拆开接住
```

### 一句话

> **`a, b = ...` 左边几个变量，右边就得凑出几个值。右边永远先算完。**

---

## 四、⭐ 什么时候可以「猜初始值」

这是最容易错的地方，判断标准只有一条：

> **这个初始值是「还没开始时的真实状态」，还是「你猜的一个数」？**

| 写法 | 对不对 | 为什么 |
| --- | --- | --- |
| `passed = 0`（计数） | ✅ | **还没数，当然是 0** —— 逻辑必然 |
| `total = 0`（累加和） | ✅ | 还没加，和是 0 —— 逻辑必然 |
| `maxss = 0`（最大值） | ❌ | **不知道数据里有没有比 0 小的** —— 猜的 |
| `minn = 100`（最小值） | ❌ | 不知道有没有比 100 大的 —— 猜的 |
| `maxss = None` | ⚠️ | 思路对，但**每个用到它的地方都要判 `is None`**，容易漏（D05 就漏了） |

**结论**：能「数」的用 0，能「加」的用 0，**要「比大小」的别猜 —— 用列表 + `max()` / `min()`。**

---

## 五、pass

```python
pass        # 空语句，什么都不做
```

**为什么要它**：Python 靠缩进划分代码块，**一个块里必须至少有一条真语句**。注释不算。

```python
if x > 0:
    # 还没想好写什么
```
↑ 报错 `IndentationError: expected an indented block`

```python
if x > 0:
    pass          # ✅ 占位，回头再填
```

**正经用途**：函数骨架、空类、故意吞异常的 `except`。

---

## 六、别再手写这些（Python 有现成的）

| 你想干的事 | 别手写 | 用现成的 |
| --- | --- | --- |
| 求和 | 累加器 `total += x` | `sum(scores)` |
| 最大 / 最小 | 猜初始值 + 循环比较 | `max(scores)` / `min(scores)` |
| 排序 | 双层循环 + 手写交换 | `scores.sort(reverse=True)` |
| 计数 | 循环 + `+= 1` | `len(scores)`（有条件时用 `sum(1 for x in s if x >= 60)`） |

**手写一遍是为了搞懂原理，搞懂之后就用现成的。** 这不是偷懒，是把时间省给真正的问题。

⚠️ **`sort()` 和 `sorted()` 的区别**：

```python
scores.sort(reverse=True)      # 原地排序，改原列表，返回 None
new = sorted(scores)           # 返回新列表，原列表不动
```

> **记忆法：带 `ed` 的（`sorted`）是「给你一个新的」；不带 `ed` 的（`sort`）是「就地改自己」。**

---

## 七、方法：`对象.动作(参数)`

```python
scores . sort ( reverse = True )
  ↑      ↑   ↑      ↑      ↑
 谁    动作  参数名   值
```

**同一个形状你已经用过好几个了：**

| 写法 | 意思 |
| --- | --- |
| `scores.append(x)` | 让 scores **追加** x |
| `scores.sort()` | 让 scores **排序** |
| `scores.sort(reverse=True)` | 让 scores **反过来排序**（降序） |
| `score.lower()` | 让 score 变成**小写** |

### `sort()` 的两种模式

```python
s = [59, 100, 85]

s.sort()                    # [59, 85, 100]   升序（默认）
s.sort(reverse=True)        # [100, 85, 59]   降序
```

**为什么参数名是 `reverse`（反过来）而不是 `descending`（降序）？**
Python 的思路是：「**默认升序，你要不要反过来？**」所以参数就叫 `reverse`。

### ⚠️ 括号里的 `=` 不是赋值

```python
reverse = True              # ← 赋值：创建一个变量 reverse
scores.sort(reverse=True)   # ← 传参：告诉 sort 用「反过来」模式
```

**写法一样，含义完全不同。** 这叫**关键字参数**，好处是不用记参数顺序：

```python
scores.sort(reverse=True)   # ✅ 清楚
scores.sort(True)           # ⚠️ 能跑，但别人看不懂 True 是什么
```

### ⚠️ `.sort()` 返回 `None`

```python
s = [59, 100, 85]
r = s.sort()
print(r)      # None            ← 返回 None！
print(s)      # [59, 85, 100]   ← 但 s 本身被改了
```

| 写法 | 改原列表？ | 返回什么 |
| --- | --- | --- |
| `s.sort()` | ✅ 改 | `None` |
| `sorted(s)` | ❌ 不改 | 新的排好序的列表 |

---

## 八、C 习惯在 Python 里多余的东西 ⚠️

**你从 C 转过来的，这些会反复绊你。**

| C 的写法 | Python |
| --- | --- |
| `int i;` 先声明变量 | 直接赋值就创建了 |
| `int temp;` / `temp = None` 占位 | **不需要**，第一次赋值就创建 |
| `for (i=0; i<n; i++)` | `for x in list` |
| `arr[i]` 取值 | 直接 `for x in arr` |
| `for (i=0; i<strlen(s); i++)` | `for i, ch in enumerate(s)` |
| `strlen(s)` | `len(s)` |
| 每行结尾 `;` | 不需要 |
| `== 0` 判空 | 直接 `if not lst:` |

> **判断方法：如果一个写法是为了「让编译器满意」而存在的，Python 里通常就不需要。**

### 例：数值交换

```c
/* C 必须用临时变量 */
temp = a;
a = b;
b = temp;
```

```python
# Python：元组解包，右边先全部算完再赋值
a, b = b, a
```

C 风格在 Python 里也能写（`k = a; a = b; b = k`），但有个**顺序陷阱**：三行里只要顺序写错，旧值就被覆盖丢了。元组解包没有这个问题。

---

## 九、踩过的坑（都是真的踩过的）

| 坑 | 现象 | 正确做法 |
| --- | --- | --- |
| 缩进混用 | `IndentationError: unindent does not match` | 统一 4 个空格，别混 Tab |
| `if score =="p" or "P":` | 恒为真 —— **`or` 返回的是操作数，不是布尔值** | `score.lower() == "p"` |
| 用 `max` / `min` / `sum` 当变量名 | 遮蔽内置函数，之后调不了 | 起名 `maxss` / `minn` |
| 改一半 | 初始值从 `0` 改成 `None`，忘了加 `is None` 判断 → 第一个数就崩 | **改一半比不改更危险**，要么全改要么不改 |
| 除零 | 直接退出时 `ZeroDivisionError` | 先判 `len(scores) == 0` |
