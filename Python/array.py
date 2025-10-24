arr1 = [0,10,33,44,90]
print(arr1)
arr1.append(11) #array.append[?]---新增加数值(?)到最后
print(arr1)
arr1[1]=99 #array[0]=22,指定列表中的第1个数值改为22
print(arr1)
print(len(arr1))

del arr1[0] #del arr1[0],删掉列表中第1个数值
print(arr1)
arr1.insert(2,88) #array.insert(2,25)
print(arr1)

arr2 = [10, 20, 30, 40, 50]
print(arr2[1:4])      #  列表中的[20, 30, 40]（取多个）
arr2[1:4] = [99, 88, 77]   #一次修改多项
print(arr2)           # [10, 99, 88, 77, 50]

arr2.extend([60, 70, 80])   # array.extend为一次加入多个数值在最后
# 结果：[10, 99, 88, 77, 50, 60, 70, 80]

arr3 = [10, 20, 30, 40, 50]
print(arr3[1:4])   # [20, 30, 40]
print(arr3[:3])    # [10, 20, 30]
print(arr3[::2])   # [10, 30, 50]（隔一个取一个）
print(arr3[::-1])  # [50, 40, 30, 20, 10] 反转

#pop
arr4 = [10, 20, 30, 40, 50]

# 删除最后一个
x = arr4.pop()
print(x)      # 输出: 50   （返回被删除的值）
print(arr4)    # [10, 20, 30, 40]

# 删除指定位置的元素（例如索引 1）
y = arr4.pop(1)
print(y)      # 输出: 20
print(arr4)    # [10, 30, 40]

arr5 = [1,9,2,8,3,7,4,6]
arr5.reverse()
print(arr5)
arr5.sort()
print(arr5)

a = [1,3]
b = [2,4]
c=a+b
print(c)
c.sort()
print(c)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[1][2])  # 6
print(matrix[1])  # [4，5，6]

matrix1 = [[0 for _ in range(3)] for _ in range(2)]# [[0, 0, 0], [0, 0, 0]]
print(matrix1)
# 内层循环 for _ in range(3)
# 我们并不在意循环变量的名字，因为只想生成 3 个 0。
# 所以就写 _。
for _ in range(3):
    print("Hello")


fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
for a, b in enumerate(fruits):
    print(a, b)
for i in range(len(fruits)):
    print(i, fruits[i])