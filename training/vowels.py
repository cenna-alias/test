str = "Mar Baselios"
vowels = "aeiouAEIOU"
vcount = 0
ccount = 0
for ch in str:
    if ch.isalpha():
        if ch in vowels:
            vcount += 1
        else:
            ccount += 1
print("Number of vowels:", vcount)
print("Number of consonants:", ccount)
