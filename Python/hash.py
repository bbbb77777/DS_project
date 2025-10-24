#print(ord('Apple')) #ord只能转换字母，字串则不行，需分开
#ord()为将字母转成数字
print(ord('A'))  # 65

def hash_function(word):
    for i in word:

        print(i,ord(i))

hash_function('Apple')  #分Apple分别输出字串

def hash_function2(word):
    total = 0
    for i in word:
        print(i,ord(i))
        total += ord(i)
    result = total%51
    print(result)


hash_function2('geng') 

score = {"Alice" : 90 , "Billie" : 100 , "Coco" : 80 , 'Alice':10}
print(score["Alice"])

names = ["Alice", "Billie", "Coco"]
values = [90, 100, 80]
score2 = dict(zip(names, values))
print(score2)
print(score2["Billie"])