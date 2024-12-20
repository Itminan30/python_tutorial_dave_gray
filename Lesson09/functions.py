def hello_world():
    print("Hello World!")
hello_world()

def add(num1, num2):
    print(num1 + num2)

add(1, 2)
add(3, 5)

def sumr(num1 = 0, num2 = 0):
    if type(num1) != int or type(num2) != int:
        return
    return num1 + num2
print(sumr(1, 2))
print(sumr('a', 3))
print(sumr())

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("a", "b", "c")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(a=1, b=2, c=3, d=4)
