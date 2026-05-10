def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = int((left + right) / 2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

list = [23, 24, 30, 34, 38, 44, 45, 49, 50, 51]

result = binary_search(list, 51)

print("result ->", list[result])