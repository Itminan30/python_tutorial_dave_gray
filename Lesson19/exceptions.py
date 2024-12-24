# Custom error
class JustNotCoolError(Exception):
    pass

x = 2
try:
    # print(x)
    # if type(x) is not str:
    #     raise TypeError('x must be a string')
    raise JustNotCoolError("Not Cool")
except NameError:
    print("Variable is probably undefined")
except ZeroDivisionError:
    print("Please don't divide by zero")
except Exception as e:
    print(e)
else:
    print("No error - Would run if there is no error")
finally:
    print("Would run no matter what!!!")