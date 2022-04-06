def remote_control_next():
    yield "cnn"
    yield "espn"


for c in remote_control_next():
    print(c)

# using generator for fibbonaci sequence

def fib():
    a, b = 0, 1
    while True:
        yield a 
        a, b = b, a+ b
    
for f in fib():
    if  f > 50:
        break
    print(f)

