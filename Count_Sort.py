def count_sort(given_list):
    max_element = given_list[0]
    min_element = given_list[0]

    for i in range(1,len(given_list)):
        if given_list[i] > max_element:
            max_element = given_list[i]
        if given_list[i] < min_element:
            min_element = given_list[i]

    numbers_range = max_element - min_element
    position_list = [0 for i in range(0,max_element+1)]

    for i in range(0,len(given_list)):
        position_list[given_list[i]]+=1

    for i in range(1,len(position_list)):
        position_list[i]+=position_list[i-1]

    sorted_list = [0]*len(given_list)
    for i in range(len(given_list)-1,-1,-1):
        sorted_list[position_list[given_list[i]]-1] = given_list[i]
        position_list[given_list[i]]-=1
        
    return sorted_list;

given_list  = [6,0,2,0,1,3,4,6,1,3,2]
sorted_list = count_sort(given_list)
print(sorted_list)
