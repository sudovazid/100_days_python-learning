x=input("Enter number1: ")
y=input("Enter number2: ")

try:
    z = x / int(y)
except Exception as e:
    print("Exception occured: ",e)
    z = None
# to find the expection type
except Exception as e:
    print("exception type: ", type(e).__name__)
    z = None
print("Division is: ",z)