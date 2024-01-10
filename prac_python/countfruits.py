fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits : 
    if fruit == '사과' :
        count += 1
        
print(count)

def count_fruits(target) : 
    count = 0
    for fruit in fruits :
        if fruit == target :
            count += 1
    return count
        
subak_count = count_fruits('수박')
print(subak_count) #수박의 갯수

gam_count = count_fruits('감')
print(gam_count) #감의 갯수