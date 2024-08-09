'''
X的Y次方
    X**Y

數字運算 
 
1.整數除法 //  
x=3//6     #得出0
x=3//0.5   #得出6.0

2.開根號 **0.5 
x=4**0.5   #得出2.0

3.取餘數 %
x=3%4      #得出3(3除與4，餘數為3)

4.替換X
x=2+3  
    print(x)    #得出x=5
x=x+1      #先看等號後面 再帶回去x (x=5+1)
    print(x)    #得出x=6
 
5.x+=1   x=x+1簡寫   
6.x-=1   x=x-1簡寫
'''
"""
字串運算   

A.雙引號前加\(可在引號內加引號)  
x="Hell\"o"
    print(x)     #得出Hell"o

B.自串串接  + 或 空格
s="hello" "world"
    print(s)     #得出helloworld

C.換行 
1.寫法1 \n  
s="Hello\nworld"    
        得出Hello
            world

2.寫法2    '''字'''   """#字"""
s="""Hello  #(中間看要空幾格)

world"""


"""
字串可加減乘
s1="Hello"*3+"world"
    print(s1)   #得出HelloHelloHelloworld

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

"""