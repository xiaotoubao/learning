#

# def SayHello():
#     print "HelloWorld!"
#
# SayHello()


def ProcessList_Modify(list, completed_list):
    """
    Process item in 'list' and move to 'completed_list' when it's done.

    :param list: work list
    :param completed_list: completed item
    :return:
    """
    while list:
        item = list.pop()
        print "item:", item
        completed_list.append(item)


# def ProcessList_Copy(list[:], completed_list): # is this Python3.0 grammar??
#     """
#     Process item in a copy of list and move to completed_list when it's done.
#
#     :param list: work list
#     :param completed_list: completed item
#     :return:
#     """
#     while list:
#         item = list.pop()
#         print "item:", item
#         completed_list


def printMax(a, b):
    """
    printMax return the bigger param

    :param a: integer A
    :param b: integer B
    :return: The bigger one between a and b
    """

    try:
        intA = int(a)
    except:
        print a, " is not an integer"
        return
    else:
        print a
    try:
        intB = int(b)
    except:
        print b, " is not an integer"
    else:
        print b
    if intA > intB:
        print intA, "is bigger than", intB
        max = intA
    else:
        print intB, "is equal or bigger than", intA
        max = intB
    if max is not None:
        return max
    else:
        return None


def Say(msg, times=1):
    print msg * times


###### main method here ######

# print printMax.__doc__

## call printMax
# while True:
#     a = raw_input("input an integer:")
#     b = raw_input("input another integer:")
#     try:
#         intA = int(a)
#         intB = int(b)
#     except:
#         print a, " or ", b , " is not an integer"
#         continue
#     else:
#         max = printMax(a, b)
#         if max is not None:
#             print "the bigger number is ", max
#         break


### call Say
# Say("Hello")
# Say("world", 3)

### call ModifyList
# print ModifyList.__doc__
#
# work_item = ['abc', '123', 'you']
# completed_item = []
# ModifyList(list=work_item, completed_list=completed_item)
# print "work_item", work_item
# print "completed_item", completed_item

def test(
        p1, p2, p3,
        p4, p5, p6
):
    shortlist = [p1, p2, p3, p4, p5, p6]
    print shortlist


test(1, 3, 5, 7, 9, 11)
