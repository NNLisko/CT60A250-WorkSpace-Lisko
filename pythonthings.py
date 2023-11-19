def part(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def qS(array, low, high):
    if low < high:

        pi = part(array, low, high)
        qS(array, low, pi - 1)
        qS(array, pi + 1, high)

data = [12, 4, 64, 673, 2, 3, 6, 43, 86, 34]
print(f"Unsorted array\n{data}")
size = len(data)
qS(data, 0, size - 1)
print(f"Sorted array in ascending order:\n{data}")

##############################################################################

def Qs(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [item for item in array[1:] if item < pivot]
        right = [item for item in array[1:] if item >= pivot]
        return Qs(left) + [pivot] + Qs(right)
    
data2 = [12, 4, 64, 673, 2, 3, 6, 43, 86, 34]
sorted_array = Qs(data2)
print(f"Sorted array in ascending order:\n{sorted_array}")
