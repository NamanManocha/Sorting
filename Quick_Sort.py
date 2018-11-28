def partition(array, low, high):

    if low < high:
        print(low, high)
        j = quick_sort(array,low,high)
        print(array[j])
        partition(array,low,j)
        partition(array,j+1,high)


def quick_sort(array, low, high):
    pivot = array[low]
    i=low+1
    j=high
    print(array[j],"Helloo ", pivot)
    
    while(i<j):
        while(array[i] < pivot):
            i+=1
        while(array[j] >= pivot):
            j-=1
        if i<j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            
    temp = array[low]
    array[low] = array[j]
    array[j] = temp
    return j;
    

array = [9,4,10,72,2,1,7,8]
partition(array, 0, len(array)-1)
print(array)
