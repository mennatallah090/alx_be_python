def greet(name):
    message="hello"
    print(f"{message} {name}!")

greet("menna")

def rec(length, width):
    area = length * width
    return area
print(rec(5,10))

def check(num):
    if num % 2 == 0:
        print("number is even.")
    else:
        print("number is odd.")

check(2)