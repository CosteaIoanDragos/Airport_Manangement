def mySearch(lst, f):
    '''
    Determine all elements from the list that staisfy the given criteria f.
    '''
    result = []
    for i in range(len(lst)):
        if f(lst[i]):
            result.append(lst[i])
    return result
def mySearch1 (lst,f):
    """
    determines if an element is in a list
    :param lst:
    :param f:
    :return:
    """
    for i in range(len(lst)):
        if f(lst[i]):
            return True
    return False
def mySort(lst, f):
    """
    Sorts a list that setisfys critarea f
   """
    for i in range(len(lst)):
        for j in  range(len(lst)-i-1):
            if f(lst[j], lst[j+1]) == False:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst