n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(j, end=' ')
    print()

n = int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(j, end=' ')
    print()