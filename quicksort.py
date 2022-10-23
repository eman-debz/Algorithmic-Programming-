def quicksort(values):
    if len(values) <= 1:  # base case
        return values
    less_than = []
    greater_than = []
    pivot = values[0]
    print(pivot)
    for i in values[1:]:  # for every value except pivot
        if i <= pivot:
            less_than.append(i)
        else:
            greater_than.append(i)
    return quicksort(less_than) + [pivot] + quicksort(greater_than)


num_list = [7,3,9,12,17]
sorted_list = quicksort(num_list)
print(sorted_list)

# O(Log n) decent complexity