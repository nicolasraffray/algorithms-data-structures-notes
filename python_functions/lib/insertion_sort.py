def insersion_sort(array):
    for i in range(0, len(array)):
        check = array[i]
        pointer = i - 1
        while pointer > 0 and check < array[pointer]:
            array[pointer + 1] = array[pointer]
            pointer -= 1
        array[pointer + 1] = check
    return array
