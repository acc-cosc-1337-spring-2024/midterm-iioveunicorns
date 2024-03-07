#write functions here, don't add input('') statements here!
x = 20

def use_global():
    global x
    x = x + 1
    print("Inside function x: ", x)

use_global()
print("Outside function x: ", x)
