"""Lists defines simple list related operations"""
# finishing up the class exercises
def get_first_item(li):
    """Return the first item from the list"""
    print(li)
    return li[0]
    

def get_last_item(li):
    return len(li)-1
    """Return the last item from the list"""
    
    

def get_second_and_third_items(li):
    return li[1], li[2]
    """Return second and third item from the list"""
    
    

def get_sum(li):
    """Return the sum of the list items"""
    sum=0
    for i in li:
        sum+=i
    return sum
    

def get_avg(li):
    """Returns the average of the list items"""
    sum=get_sum(li)
    print(li)
    print(sum)
    
    return sum/len(li)
    
    
