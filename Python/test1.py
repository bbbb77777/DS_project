#Google Interview Question
#Give an array =[1,2,3,4,2,3,4,5]
#return 2

#Give an array =[1,2,1,4,2,3,4,5]
#return 1

#Give an array =[1,2,3,4]
#return undefined
#找出array中第一个重复的字符

def arr1 (word):
    seen = set()#set() or []
    for i in word:
        if i in seen:
            return i
        seen.add(i)#若上面用set,则用add。若上面为[],则用append
    return 'Undefined'


print(arr1([1,1,2,3]))# 输出：1
print(arr1([1,5,2,3,6,7,8,9,10,3]))# 输出：3
print(arr1([1,2,3,4,5]))# 输出：Undefined