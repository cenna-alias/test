s = "banana"
visited = ""

for i in range(len(s)):
    if s[i] not in visited:
        count = 0

        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1

        print(s[i], "-", count)
        visited += s[i]