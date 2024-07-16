s1=('https://www.youtube.com/results?search_query=LiSA-ADAMAS'.partition('='))
#先將字串分割成三段，以=為區分標準
print(s1[2].replace('+',' '))       
#取字串中的第三段，並將+號替代成空格。

s1=('youtube.com/results?search_query=YOASOBI+-+Idol'.partition('=')) 
print(s1[2].replace('+',' '))

s1=('www.youtube.com/results?search_query=I+want+it+that+way'.partition('='))
print(s1[2].replace('+',' '))