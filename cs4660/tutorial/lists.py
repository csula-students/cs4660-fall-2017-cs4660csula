"""Lists defines simple list related operations"""
# finishing up the class exercises
def get_first_item(li):
    """Return the first item from the list"""
    print(li)
    return li[0]
    pass

def get_last_item(li):
    """Return the last item from the list"""
    return len(li)-1
    pass

def get_second_and_third_items(li):
    """Return second and third item from the list"""
    li[1], li[2]
    pass

def get_sum(li):
    """Return the sum of the list items"""
    sum=0
    for i in li:
        sum+=i
    return sum
    pass

def get_avg(li):
    """Returns the average of the list items"""
    sum=get_sum(li)
    print(li)
    print(sum)
    
    return sum/len(li)
    pass
    
