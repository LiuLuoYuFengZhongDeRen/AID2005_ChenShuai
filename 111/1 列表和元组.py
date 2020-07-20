# 《列表和元组》--序列类型（Sequence Types — list, tuple, range ）中的两种。
# 《列表》
# 1.定义：写作中括号之间的一列逗号分隔的值。
squares1 = [1, 4, 9, 16, 25]
print(squares1)
for i in squares1:
    print(i)

# 2.特点：
# (2.1)列表的元素不必是同一类型(允许嵌套列表-创建一个包含其它列表的列表)
squares2 = [1, '44', 6.32, [1, 2], {'name': 'Jack Chen'}]
print(squares2)
for i in squares2:
    print(i)

# (2.2)列表可以被索引和切片,所有的切片操作都会返回一个包含请求的元素的新列表
squares = [1, 4, 9, 16, 25]
print(squares[0])  # indexing returns the item
print(squares[-3:])  # slicing returns a new list

# (2.3)列表是可变的，它允许修改元素
cubes = [1, 8, 27, 65, 125]  # something's wrong here
cubes[3] = 64  # replace the wrong value
print(cubes)

# (2.4)列表可以使用的一些方法
# len(listObject)：返回一个列表的长度
s = [1, 2, 3, 4]
print(len(s))

# list.append(x):把一个元素添加到列表的结尾
list = [1, 2, 3]
list.append(4)
print(list)

list[len(list):] = [5]
print(list)

# list.extend(L)：将一个给定列表中的所有元素都添加到另一个列表中，相当于 a[len(a):] = L
list = [1, 2, 3]
l = [4, 5, 6]
list.extend(l)
print(list)
l2 = [7,8,9]
list = list+l2
print(list)
list[len(list):] = [10, 11, 12]
print(list)

# list.insert(i, x)：在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x)。
list = [1, 2, 3]
list.insert(0, 0)
print(list)
list.insert(4,4)
print(list)

# list.remove(x)：删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list = [1, 1, 2, 2, 3]
list.remove(1)
print(list)
list.remove(4)

# list.pop([i])：从列表的指定位置删除元素，并将其返回。
# 如果没有指定索引，a.pop() 返回最后一个元素。元素随即从列表中被删除（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在Python 库参考手册中遇到这样的标记）。
list = [1, 2, 3, 4, 5, 6]
a = list.pop()
print(a)
print(list)
b = list.pop(4)
print(b)
print(list)

# list.clear()：从列表中删除所有元素。相当于 del a[:]。
list = [1, 2, 3]
list.clear()
print(list)

# list.index(x, start, stop)：返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list = [11, 22, 33, 44, 55, 22, 11]
index = list.index(22)
print(index)
index = list.index(22, 2, 7)
print(index)
index = list.index(33, 2, 7)
print(index)

# list.count(x)：返回 x 在列表中出现的次数。
list = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 2, 5, 6]
print(list.count(6))
intNumber = 4
print("list列表中为 {0} 的整数总共有 {1} 个".format(intNumber, list.count(intNumber)))

# list.sort()：对列表中的元素就地进行排序。
list = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 2, 5, 6]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
from operator import itemgetter
list = [('a', 1, 'c'), ('d', 2, 'e'), ('f', 3, 'g'), ('h', 4, 'i'), ('j', 5, 'k')]
list.sort(key=itemgetter(1), reverse=False)
print(list)
list = [('a', 1, 'c'), ('d', 2, 'e'), ('f', 3, 'g'), ('h', 4, 'i'), ('j', 5, 'k'), ('b', 1, 'c')]
list2 = sorted(list, key=itemgetter(0), reverse=True)
print(list2)
list3 = sorted(list2, key=itemgetter(1), reverse=False)
print(list3)

# list.reverse()：就地倒排列表中的元素。
list = [1, 2, 3]
list.reverse()
print(list)

# list.copy()：返回列表的一个浅拷贝。等同于 a[:]。
list = [1, 2, 3]
copy_list = list.copy()
print(copy_list)
copy_list.append(4)
print(copy_list)
print(list)

# (2.4)列表当堆栈使用：堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
s = stack.pop()
print(s)
print(stack)


# (2.5)列表当队列使用：队列作为特定的数据结构，最先进入的元素最先释放（先进先出）。不过，列表这样用效率不高。相对来说从列表末尾添加和弹出很快；在头部插入和弹出很慢（因为，为了一个元素，要移动整个列表中的所有元素）。
# 要实现队列，使用 collections.deque，它为在首尾两端快速插入和删除而设计。
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")          # Terry arrives
queue.append("Graham")         # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
print(queue)                    # Remaining queue in order of arrival


# 《元组》
# 1.定义：一个元组由数个逗号分隔的值组成
t = 12345, 54321, 'hello!'
u = t, (1, 2, 3, 4, 5)

# 2.特点
# (2.1)输入输出格式：在输入时可以有或没有括号，不过经常括号都是必须的（如果元组是一个更大的表达式的一部分）。元组在输出时总是有括号的，以便于正确表达嵌套结构。
# (2.2)赋值：元组就像字符串，不可变的。不能给元组的一个独立的元素赋值（尽管你可以通过联接和切割来模拟，还可以创建包含可变对象的元组，例如列表）。
# (2.3)访问：通常包含不同种类的元素并通过分拆或索引访问（如果是 namedtuples，甚至可以通过属性）。
# (2.4)构造包含零个或一个元素的元组：一对空的括号可以创建空元组；要创建一个单元素元组可以在值后面跟一个逗号（在括号中放入一个单值不够明确）。
# (2.5)元组元素不可变的理解：tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
#      理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。

# 《一些循环技巧引用在列表和元组中》
# 在序列中循环时，索引位置和对应值可以使用 enumerate() 函数同时得到:
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 同时循环两个或更多的序列，可以使用 zip() 整体打包:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# 需要逆向循环序列的话，先正向定位序列，然后调用 reversed() 函数:
for i in reversed(range(1, 10, 2)):
    print(i)
# 要按排序后的顺序循环序列的话，使用 sorted() 函数，它不改动原序列，而是生成一个新的已排序的序列:
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
# 若要在循环内部修改正在遍历的序列（例如复制某些元素），建议您首先制作副本。在序列上循环不会隐式地创建副本。切片表示法使这尤其方便。
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)
