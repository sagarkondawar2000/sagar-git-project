def merge_sort(arr):
    """Sorts an array using the merge sort algorithm.

    Args:
        arr: The array to be sorted.

    Returns:
        The sorted array.
    """

    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left_half, right_half):
    """Merges two sorted arrays into a single sorted array.

    Args:
        left_half: The left half of the array.
        right_half: The right half of the array.

    Returns:
        The merged sorted array.
    """

    merged = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    merged.extend(left_half[i:])
    merged.extend(right_half[j:])

    return merged

# Example usage:
my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_array = merge_sort(my_array)
print(sorted_array)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
