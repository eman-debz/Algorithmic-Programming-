def selection_sort(values):
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list


def index_min(values):
    min_index = 0
    for i in range(1,len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index


num_list = [7,3,9,12,17]
print(selection_sort(num_list))