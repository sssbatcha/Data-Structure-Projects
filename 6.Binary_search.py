print("Binary Search:")
arr = [2, 3, 4, 10, 40]
x = 10
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == x:
        print("Element found at index:", mid)
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")                                              






    