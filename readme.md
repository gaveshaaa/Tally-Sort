# Counting Sort

Counting Sort is a simple sorting algorithm used to sort a collection of integers within a specific range

## Algorithm Overview

1. **Determine Range**: Find the maximum and minimum values in the input array to determine the range of values.
2. **Create Counting Array**: Create an array to store the frequency of each value within the determined range.
3. **Count Frequencies**: Traverse the input array and count the occurrences of each value within the range.
4. **Reconstruct Sorted Array**: Reconstruct the sorted array based on the counts in the counting array.

## Idea/Vision

The aim of this project is purely educational,
Please don't use this in any production enviorment.
Hope that goes without explicitly saying.

### Considerations

- Counting Sort works efficiently for a small range of integers.
- Arrays with significantly large values, like [500000, 4, 5, 7, 3, 1], might take considerably longer due to the
  allocation of space for the large range of values, affecting the overall performance.

## Big O Complexity

- **Time Complexity**: O(n + k), where n is the number of elements and k is the range of values.
- **Space Complexity**: O(n + k)

## Examples

### Example 1:

Input Array: [4, 2, 5, 1, 3]
Output: [1, 2, 3, 4, 5]

### Example 2:

Input Array: [100, 5, 23, 87, 1, 42, 23]
Output: [1, 5, 23, 23, 42, 87, 100]

## Improve

I dont't see much to improve in this code, its limited.
But if you have any idea or suggestions open a pull request.
I'm open to learning more.
