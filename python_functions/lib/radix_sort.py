def counting_sort(array, base):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // base
        count[index % 10] += 1

    # Calculate cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # base the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // base
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

    return output, count, array


print(counting_sort([1, 2, 3, 5, 13252, 1314, 234, 1412], 1))


def radix_sort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on base value.
    base = 1
    while max_element // base > 0:
        counting_sort(array, base)
        base *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radix_sort(data)
print(data)
