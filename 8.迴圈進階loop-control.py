'''
一定要跟迴圈搭配的指令

1.break 
    強制結束迴圈

語法:
while 布林值:
    break
    
for 變數名稱 in 列表或字串:
    break

範例A
n=1
while n<5:      n本來需要跑到5才會把迴圈結束掉
    if n==3:    但判斷式說當n=3的時候會結束迴圈
        break      Q:為什麼不會跑出1或2?
    n+=1
print(n)   

得到3


2.continue   
    強制繼續下一圈

語法:
while 布林值:
    continue
    
for 變數名稱 in 列表或字串:
    continue

範例A

n=0                     %為取餘數 整條為x被2除 如果餘數等於零 意即x被2整除
for x in [0,1,2,3]:     本來 
    if x%2==0:         
        continue        
    n+=1
print(n)
        
3.else 
    迴圈結束前，執行此區快的命令

語法:
while 布林值:
    若布林值為True，執行命令
    回到上方，做下一次的迴圈判斷
else:
    迴圈結束前，執行此區快的命令

for變數名稱in列表或字串:
    將列表中的項目或字串中的字元逐一取出，逐一處理
elsr:
    迴圈結束前，執行此區快的命令 

範例A
n=1
while n<5:
    print("變數n的資料是:",n)
    n+=1
else:
    print(n)

範例B
for c in"Hello":
    print("逐一取得字串中的字元",c)
else:
print(c)


    

'''


for c in "Hello":
    print("逐一取得字串中的字元",c)
else:
    print(c)