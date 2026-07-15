s = "abciiidef"
k = 3

vowels = {'a', 'e', 'i', 'o', 'u'}

# Count vowels in the first window
count = 0
for i in range(k):
    if s[i] in vowels:
        count += 1

maxx = count
for i in range(k, len(s)):

    # Remove the outgoing character
    if s[i - k] in vowels:
        count -= 1

    # Add the incoming character
    if s[i] in vowels:
        count += 1

    # Update maximum vowel count
    if count > maxx:
        maxx = count

    # If all characters are vowels, return immediately
    if count == k:
        print(k)
        break
else:
    print(maxx)