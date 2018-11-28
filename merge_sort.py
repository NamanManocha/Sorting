

def merge_sort(arr,l,u):
    if l<u:
        m= int((l+u)/2)
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,u)
        merge(arr,l,m,u)

def merge(arr,l,m,r):
    l_size = m-l+1
    r_size = r-m
    
    left_list = [0] * (l_size)
    right_list = [0] * (r_size)
    
    i=0
    j=0
    k=l
    for i in range(0,l_size):
        left_list[i] = arr[l+i]
    for j in range(0,r_size):
        right_list[j] = arr[m+1+j]

    i=0
    j=0
    while i<l_size and j<r_size:
        if left_list[i] <= right_list[j]:
            arr[k] = left_list[i]
            i+=1
        else:
            arr[k] = right_list[j]
            j+=1
        k+=1

    while i<l_size:
        arr[k] = left_list[i]
        i+=1
        k+=1
    while j<r_size:
        arr[k] = right_list[j]
        j+=1
        k+=1
    

