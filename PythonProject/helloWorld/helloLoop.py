
##### for #####
# for i in range(0,5):
#     print i



import helloModule

while True:
    try:
        input = int(raw_input("input an integer:"))
    except:
        print input, " is not an integer"
        continue
    else:
        print "Sqrt of ", input, " is ", helloModule.Sqrt(input), "\n"
        break
