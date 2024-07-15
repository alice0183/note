# 集合 (一群資料，沒有順序放一起)
# 判斷資料是否在集合中(in / not in)
s1={3,4,5}
print(3 in s1)     # 3是否在s1中? true

# 集合的運算
# 交集 &  (兩個集合中取相同部分)

s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2
print(s3)    #s3等於s1與s2中相同的資料{4, 5}

# 聯集 |  (兩個集合中的所有資料，但不重複取)
s1={3,4,5}
s2={4,5,6,7}
s3=s1|s2
print(s3)    #得出{3, 4, 5, 6, 7}

# 差集 -  (從s1中減去和s2重疊的部分)
s1={3,4,5}
s2={4,5,6,7}
s3=s1-s2
print(s3)    #得出{3}

# 反交集 ^ (取兩個集合中，不重疊的部分)
s1={3,4,5}
s2={4,5,6,7}
s3=s1^s2
print(s3)    #得出{3, 6, 7}


# 將字串中的字母拆解成集合 set(字串)
s=set("Hello")
print(s)        #得出{'o', 'e', 'l', 'H'} 無順序性

s=set("Hello")
print("H" in s) # H是否在字串內? True



#  字典   
#  鍵值對(Key-Value Pair) 一個索引對一個資料 一個key 對一個Value 很多對
#  字典[Key]
#  字典[Key]=Value
dic={"apple":"蘋果","bug":"蟲蟲"}
print(dic["apple"])       #輸入key(apple)得出值(蘋果) 

dic={"apple":"蘋果","bug":"蟲蟲"}
dic["apple"]="小蘋果"
print(dic["apple"])       #將蘋果修改成小蘋果 得出小蘋果


#判斷key是否存在(不會判斷value)
dic={"apple":"蘋果","bug":"蟲蟲"}
print("apple" in dic)      #apple是否存在於dic字典? True


#  del 刪除鍵值對(key跟value一起刪除) 

dic={"apple":"蘋果","bug":"蟲蟲"}
print(dic)       #得出{'apple': '蘋果', 'bug': '蟲蟲'}
del dic["apple"]
print(dic)       #得出{'bug': '蟲蟲'}
 
#  可用列表資料為基礎建立字典   for (任一字母) in 列表
dic={x:x*2 for x in [3,4,5]}    
print(dic)       
#  得出{3: 6, 4: 8, 5: 10}  key為列表中的值 value為列表中的值*2

