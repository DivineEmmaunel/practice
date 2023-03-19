
some_list =[3,7,2,9,4,5,6]

# The below code doesn't seem to find the minimum element in the list. Why?
def minimum(some_list):
    # make a = the first element on the list
    a = some_list[0]
    for x in range(1, len(some_list)):
        if some_list[x] < a:
            a = some_list[x]
            print(a)
    return a

get_minimum = minimum(some_list)
print(get_minimum)
