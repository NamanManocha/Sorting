import math

def heap_sort(array, length):
    n = math.floor(length/2)
    for i in range(n,-1,-1):
        max_heapify(array, i, length)

    for i in range(0, length):
        array[0], array[length-i] = array[length-i], array[0]
        max_heapify(array, 0, length-i-1)

def max_heapify(array, i, length):
    left = (2*i)+1
    right = (2*i)+2
    max_index = i

    if left <= length and array[left] > array[i]:
        max_index = left
    if right <= length and array[right] > array[max_index]:
        max_index = right

    if max_index!=i:
        array[max_index], array[i] = array[i], array[max_index]
        max_heapify(array, max_index, length)

array = [5,55,38,2,1,89,78,34]
heap_sort(array, len(array)-1)
print(array)
