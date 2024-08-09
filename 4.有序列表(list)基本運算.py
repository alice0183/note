'''
索引(List)(有序可變動列表) 用中括號[]

1.列表中也有索引
範例:
grades=[12,60,15,70,90]
    print(grades[0])     # 得出12
    print(grades[3])     # 得出70

2.更改列表中的數字 把55放到列表中的第一個位子
grades=[12,60,15,70,90]
grades[0]=55
    print(grades[0])     # 得出55(第一個數字變成55)  

3.連續刪除列表中從編號1到編號4(不包括)的資料
grades=[12,60,15,70,90]
grades[1:4]=[]
    print(grades)        # 得出 [12, 90] 

4.列表串接(用加法)
grades=[12,60,15,70,90]
grades=grades+[12,33]
    print(grades)        # 得出[12, 60, 15, 70, 90, 12, 33]

5.列表的長度 [len 列表(取得列表長度)]
    length=len(列表)
grades=[12,60,15,70,90]
length=len(grades)
    print(length)        # 得出5(列表長度) 


6.巢狀列表(列表中的資料也可以是列表)
date表示第一層 
date[0]=[3,4,5] 
date[1]=[6,7,8]
date=[[3,4,5],[6,7,8]]
    print(date[1][2])          # 得出8
 
date=[[3,4,5],[6,7,8]]
date[0][0:1]=[3,3,3]       # 將第一格之中第一個資料[3]去除更改為[3,3,3]
    print(date[0])             # 得出[3, 3, 3, 4, 5]


Tuple(有序資料不可更動) 用小括號()
    所有操作都跟List一樣，但是不可變動值

data=(3,4,5)
data[0]=5      #錯誤 Tuple資料不可更動
    print(data[0:2])

'''