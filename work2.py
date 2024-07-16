s1=('https://www.youtube.com/results?search_query=YOASOBI+-+Idol')
s2=(s1[45:])
s3=s2.partition('-')
print(s3[0].strip('+')+s3[1]+s3[2].strip('+'))