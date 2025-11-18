import math
a = input("num: ")
def checknum(x):
        try:
            float(x)
        except ValueError:
            print("not a numb")
            return False
        else:
            print("a num")
            return True

            

        