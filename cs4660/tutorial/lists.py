
def get_first_item(li):
    return li[0]
    

def get_last_item(li):
    return li-1
    
    

def get_second_and_third_items(li):
    return li[1], li[2]
     
    

def get_sum(li):
    sum=0
    for i in li:
        sum+=i
    return sum
    

def get_avg(li):
    sum=get_sum(li)
    return sum/len(li)