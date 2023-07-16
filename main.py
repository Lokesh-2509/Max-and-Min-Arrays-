def sum_of_max_and_min(arr):
    min_val = min(arr)
    max_val = max(arr)
    return min_val + max_val
A = [-2, 1, -4, 5, 3]
result = sum_of_max_and_min(A)
print("Sum of maximum and minimum elements:", result)
A = [1, 3, 4, 1]
result = sum_of_max_and_min(A)
print("Sum of maximum and minimum elements:", result)
