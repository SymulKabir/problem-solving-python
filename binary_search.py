def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

list = [154, 149, 120, 87, 34, 40]

result = binary_search(list, 34)

print("result -->>", result)
# print("result -->>", list[result])
