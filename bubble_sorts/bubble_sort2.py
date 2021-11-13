def bubble(array):
    n = len(array)
    for i in range(n-1):
        flag = 0
        for j in range(n-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                flag = 1
        if flag == 0:
            break
    return array


array = [6,7,5,4,5,6,4,3,2,1,10]

result = bubble(array)



print(result)


#https://www.guru99.com/bubble-sort.html
#https://stackabuse.com/bubble-sort-in-python/

