def binary_search(arr, target):
    left, right = 0, len(arr) - 1 
    while left <= right:
        mid = int(left + ((right - left) / 2))
        print("left ->", left)
        print("right ->", right)
        print("mid ->", mid)
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
    
    
    



async_list = [34, 87, 120, 149, 154, 160, 170, 180]

result = binary_search(async_list, 87)

print("result -->>", result)
print("result -->>", async_list[result])
