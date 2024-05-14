def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is not None:
        return (iterations, upper_bound)
    else:
        return (iterations, None)

# Тест
sorted_array = [1.1, 2.3, 3.5, 4.7, 5.9, 6.8, 7.6, 8.0, 9.3]
target = 5.5

result = binary_search(sorted_array, target)
print(f"Iterations: {result[0]}, Upper Bound: {result[1]}")  
