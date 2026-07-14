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

#using dictionary  
str = "banana"
freq = {}
for ch in str:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

#using keys
for key in freq:
    print(key,"-",freq[key])
