   def mergeTwoLists(self, l1, l2):
        """
        :type l1: array
        :type l2: array
        :rtype: array
        """
        rList = []
        if not l1 or l2:
            return l1 or l2
        else:
            if l1[0]<l2[0]:
                rList.append(l1[0])
                rList += mergeTwoLists(l1[1:],l2)
            else:
                rList.append(l2[0])
                rList += mergeTwoLists(l1,l2[1:])
                
        return rList
