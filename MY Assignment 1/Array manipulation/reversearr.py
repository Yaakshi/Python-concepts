def reverseArray(a):
    return a[::-1]      #arr[start:end:step]

arr_count = int(input("Array count: ").strip())
arr = list(map(int, input("Array: ").rstrip().split()))
res = reverseArray(arr)
print("Reversed array: ")
print(' '.join(map(str, res)))