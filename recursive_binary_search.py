def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return "not found"
    
        
    mid = int((low + high) / 2)
    
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        low = mid + 1
        return binary_search(arr, target, low, high)
    else:
        high = mid - 1
        return binary_search(arr, target, low, high)
    
    
    
arr = [12, 13, 14, 20, 21, 24, 30, 40, 44]
result = binary_search(arr, 44)

print("result ->", result)
print("result ->", arr[result])
