def moduleArray(arr, b):
    ans = 0
    pow = 1
    for i in range(len(arr)-1, 0, -1):
        ans = (ans + ((arr[i] % b) * pow) % b)
        pow = (pow * 10) % b
    return ans % b

n = int(input())
arr = list(map(int, input().split()))
b = int(input())
value = moduleArray(arr, b)
print(value)
