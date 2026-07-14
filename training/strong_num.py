n = int(input("Enter a number: "))
temp = n
sum = 0

while temp > 0:
    rem = temp % 10
    fact = 1
    for i in range(1, rem + 1):
        fact *= i
    sum += fact
    temp //= 10

if sum == n:
    print(n, "is a Strong number")
else:
    print(n, "is not a Strong number")
    