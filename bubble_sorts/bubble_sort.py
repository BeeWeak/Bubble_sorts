def bubble_sort(array):
    swapped = True
    length = len(array)
    while(swapped):
        swapped = False
        for i in range(0,length-1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i+1], array[i]
                swapped = True




array = [8,7,5,4,3,4,5,10]
bubble_sort(array)


for i in range(len(array)):
    print(array[i])
                
#https://stackabuse.com/bubble-sort-in-python/


