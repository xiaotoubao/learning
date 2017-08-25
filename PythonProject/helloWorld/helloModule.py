#! /usr/bin/python
#Filename: helloModule.py


import sys

# print 'The command line arguments are: '
# for i in sys.argv:
#     print i
# print '\n\n PYTHONPATH is ', sys.path, '\n'
#


def Sqrt(a):
    """
    Sqrt return a * a

    :param a:integer
    :return: square value of param a
    """

    if __name__ == "__main__":
        print "Sqrt() is called by itself"
    else:
        print "Sqrt() is called by", __name__
    try:
        intA = int(a)
    except:
        print a, " is not an integer"
        return None
    else:
        return a**2


# while True:
#     try:
#         input = int(raw_input("input an integer:"))
#     except:
#         print input, " is not an integer"
#         continue
#     else:
#         print "Sqrt of ", input, " is ", Sqrt(input), "\n"
#         break
