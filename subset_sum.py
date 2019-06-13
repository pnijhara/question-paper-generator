def subsetsum(array,num):

    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0].marks == num:
            return [array[0]]
        else:
            x = subsetsum(array[1:],(num - array[0].marks)) 
            if x:
                return [array[0]] + x
            else:
                return subsetsum(array[1:],num)
