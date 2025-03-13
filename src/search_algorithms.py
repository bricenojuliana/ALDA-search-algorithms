def linear_search(arr, x):
    """
    Performs a linear search on the given array to find the element x.

    Parameters:
        arr (list): The list in which to search.
        x: The element to search for.

    Returns:
        int: The index of the element if found, otherwise -1.

    Time Complexity:
        - Worst case: O(n), where n is the size of the array.
        - Best case: O(1) (when the element is at the first position).
        - Average case: O(n).
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    """
    Performs a binary search on the given sorted array to find the element x.

    Parameters:
        arr (list): The sorted list in which to search.
        x: The element to search for.

    Returns:
        int: The index of the element if found, otherwise -1.

    Time Complexity:
        - Worst case: O(log n), where n is the size of the array.
        - Best case: O(1) (when the element is at the middle position).
        - Average case: O(log n).

    Note:
        The array must be sorted for binary search to work correctly.
    """
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

def ternary_search(arr, x):
    """
    Performs a ternary search on the given sorted array to find the element x.

    Parameters:
        arr (list): The sorted list in which to search.
        x: The element to search for.

    Returns:
        int: The index of the element if found, otherwise -1.

    Time Complexity:
        - Worst case: O(log3 n), where n is the size of the array.
        - Best case: O(1) (when the element is at one of the mid positions).
        - Average case: O(log3 n).

    Note:
        The array must be sorted for ternary search to work correctly.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        if x < arr[mid1]:
            right = mid1 - 1
        elif x > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1