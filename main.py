def copy_sort(arr):

    # We first find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # Then we initalize a array with value of 0
    count_array = [0] * (max_val - min_val + 1)

    # Then we store the frequency of each element in the count array
    for num in arr:
        count_array[num - min_val] += 1

    # Reconstruct the sorted array
    sorted_array = []

    # Then we compare each other and remove unwanted numbers from the
    # newly initiated array
    for i, count in enumerate(count_array):
        value = i + min_val
        for _ in range(count):
            sorted_array.append(value)

    # Then we return the array
    return sorted_array

print(copy_sort([700, 4, 5, 7, 3, 1]))


