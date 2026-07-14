str = "banana"
count = 0
visited = set()
for i in range(0,len(str)-1):
    count = 1
    if str[i] in visited:
        break
    for j in range(i+1,len(str)):
        if str[i] == str[j]:
            count += 1
    print(str[i],"-",count)
    visited.add(str[i])