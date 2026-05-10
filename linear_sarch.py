import random

def linear_search(arr, target):
    checks = 0

    for i in range(len(arr)):
        checks += 1
        if arr[i] == target:
            return i, checks  # found index + checks

    return -1, checks  # not found


# Generate 100 random values
import random

arr = []
for i in range(100):
    arr.append(random.randint(1, 100))

index, checks = linear_search(arr, 42)

print("Array:", arr)
print("Index of 42:", index)
print("Checks:", checks)