def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Selection sort function
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))