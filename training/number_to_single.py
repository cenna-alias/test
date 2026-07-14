n = int(input("Enter number to convert to single digit: "))
temp = n
sum = 0
while temp>9:
    sum = 0
    while temp > 0:
        rem = temp%10
        sum += rem
        temp //= 10
    temp = sum
print("Single digit:", temp)