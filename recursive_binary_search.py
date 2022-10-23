def recursive_binary_search(list, target):  # Define the function
    if len(list) == 0:
        return False
    else:
        middle = (len(list))//2
        if list[middle] == target:  # IF middle index is targer 
            return True  # Return middle as it is target
        else:
            if list[middle] < target:  # IF target larger then middle discard first half 
                return recursive_binary_search(list[middle + 1:], target)
            else:  # Else discard last half of list
                return recursive_binary_search(list[:middle], target)    


def verify(search):
    print("Target found:", search)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(numbers, 7)
verify(result)

# Space Complexity O(log n)
