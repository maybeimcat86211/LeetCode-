nums = [2,1,5,3]
target = 4

# #先創建一個dict用作雜湊表
# hashtable = {}
# #迭帶 傳進來的list
# for index , value in enumerate(nums):
# #變數num=用target去減nums的每一個value 
#     num = target - value
# #如果該值不存在於雜湊表,那就存起來
#     if num not in hashtable:
#         hashtable[value] = index
#     else:
#         #return [hashtable[num],index]
#         print([hashtable[num],index])
# #假設 nums = [2,7,11,15]
# def  bruteforce(*arg):
#     #先取得nums的總數
#     # i = 0  為第一個元素
#     for i in range(len(nums)):
#         #0+1=1 ,總長度len(nums) = 4 
#         #1+1=2
#         #...etc
#         #1~4開始循環,排除第一個元素
#         for j in range(i + 1, len(nums)):
#             #if  j==7 and  j == 9 - 2 那就return
#             if nums[j] == target - nums[i]:
#                 return [i, j]
#                 print([i,j])

#字典使用方法
#https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-533b8d8d96f3
hashmap = {}
for index,value in enumerate(nums):
    diff = target - value
    #如果已經存在於雜湊表,那就回傳結果
    if diff in hashmap:
        print( [hashmap[diff],index])
    #nums這個list的每一個element變成雜湊表的key
    #把雜湊表的value設定成 當前nums的index   
    #前面是dict的key , 後面是是dict的value
    hashmap[value] = index
print(hashmap)

'''
fuck = {}
abc = ["a","b","c","d","e"]
for index,value in enumerate(abc):
    #print(value)
    #前面是dict的key , 後面是是dict的value
    fuck[index] = value
    
print(fuck)
'''