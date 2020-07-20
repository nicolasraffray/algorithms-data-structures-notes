def merge_sort(array):
    if len(array) < 2:
        return array

    mid_point = len(array) // 2
    left = array[:mid_point]
    right = array[mid_point:]

    def merge(left, right):
        result = []
        leftInd, rightInd = 0, 0

        while leftInd < len(left) and rightInd < len(right):
            if left[leftInd] < right[rightInd]:
                result.append(left[leftInd])
                leftInd += 1
            else:
                result.append(right[rightInd])
                rightInd += 1
        result += left[leftInd] + right[rightInd]
        return result

    return merge(merge_sort(left), merge_sort(right))
