"""
A. 
if 布林值:
    若布林值為 True 則會執行命令
tab鍵 (縮排，可將上下行連結成一個段落)


B.
if 布林值:
    若布林值為 True 則會執行命令
else:
    若布林值為 False 則會執行命令

    
C.
if 布林值一:
    若布林值一為 True 則會執行命令
elif 布林值二:
    若布林值二為 True 則會執行命令
else:
    若布林值一和二都 False 則會執行命令


#舉例
x=input("請輸入數字:")  基本輸入為字串型態
x=int(x)   轉換為整數型態
if x>200:
    print("大於200")
elif 200>x>100:
    print("大於100,小於200")
else:
    print("小於100")


其他語法:switch

"""
"""
示範

1.
if True:
    print("True 執行")
        得出 True 執行

2.
if False:
    print("True 執行")
        程式不會運作

3.
if True:
    print("True 執行")
else:
    print("False 執行")
        得出 True 執行

4.
if False:
    print("True 執行")
else:
    print("False 執行")
         得出 False 執行


判斷式

1.          

"""

x=input("請輸入數字:") # 取得字串形式的使用者輸入
x=int(x) #將字串型態轉換成數字型態
if x>100:
    print("大於100")
else:
    print("小於等於100")

