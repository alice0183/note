# X的Y次方=X**Y
# 數字運算  
# 整數除法 // (x=3//6)
# 開根號 (x=3**0.5)
# 取餘數 %
# x=2+3
# x=x+1 先看等號後面 再帶回去X
# x+=1   x=x+1簡寫   
# x-=1   x=x-1簡寫

# 字串運算   

# 雙引號前加\(可在引號內加引號)  "Hello\"o"

# 自串串接  + 或 空格

# 換行 \n 或 '''字''' """字"""
s="""Hello  #(中間看要空幾格)
world"""

# 字串可加減乘
# 字串會對內部的字元編號(索引)，從0開始算起
# 範例1 (含開頭編號不含結尾編號)
s='Hello' 
print(s[0:3])  # 得出Hel(012)

# 範例2 (從給的字串編號開始算起後面全部的字元)
s='Hello' 
print(s[3:])   # 得出lo(34)

# 範例3 (從給的字串編號開始算起前面全部的字元)
s='Hello' 
print(s[:4])   # 得出Hell(0123)

