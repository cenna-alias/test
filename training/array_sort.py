arr = [2, 4, 5, 6]
is_sorted = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Array is already sorted.")
else:
    print("Array is not sorted.")
    