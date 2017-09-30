def mergeTwolists(self, l1, l2)
    """
    :type l1: array
    :type l2: array
    :rtype: array
    """
    rList = []
    while l1 and l2:
        if l1[0] < l2[0]:
            l.append(l1.pop(0))
        else:
            l.append(l2.pop(0))
    return rList + a + b
                
     
