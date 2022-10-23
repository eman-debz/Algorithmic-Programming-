def recursive_sum(values):
    if not values:
        return 0
    remaining_sum = recursive_sum(values[1:])
    return values[0] + remaining_sum


print(recursive_sum([1,2,3,4,5]))
