# find the total of two list

tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

total = 0
for item in tom_exp_list:
    total = total + item
print("Tom's total experiences: ", total)

total = 0
for item in joe_exp_list:
    total = total + item
print("Joe's total experiences: ", total)

# encapsulte same for loop in function
def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

toms_total=calculate_total(tom_exp_list)
joe_total=calculate_total(joe_exp_list)

print("Tom's total expenses is: ", toms_total)
print("Joe's total expenses is: ", joe_total)

# sum of two number
def sum(a, b):
    print("a: ",a)
    print("b: ",b)
    total = a + b
    return total

n = sum(b=5,a=6) # named arguments
print("Total:", n)