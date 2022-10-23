def binary_search(list, target):  # Define the function
    first = 0  # first index of list
    last = len(list) - 1  # Last index of list

    while first <= last:
        middle = (first + last) // 2  # Find middle of list using floor div
        if list[middle] == target:  # IF middle index is targer 
            return (middle)  # Return middle as it is target   
        elif list[middle] < target:  # IF target larger then middle discard first half 
            first = (middle + 1)
        else:  # Else discard last half of list
            last = (middle - 1)

    return None


def verify(search):
    if search is not None:
        print("Target is at index", search)
    else:
        print("Algorithm didnt find target")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 7)
verify(result)

# Space Complexity O(log n)(1) Or Constant