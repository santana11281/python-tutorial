def itemInCommon(list1_, list2_):
    for i in list1_:
        for j in list2_:
            if i == j:
                return True
    return False


def itemInCommonV2(list1_, list2_):
    myDic = {}
    for i in list1_:
        myDic[i] = True
    for j in list2_:
        if j in myDic:
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(itemInCommonV2(list1, list2))
