# list

numbers=[1,2,3,4,5,6,7]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)

print(even)

# list conprehension
even = [i for i in numbers if i%2 == 0]
print(even)

# square of numbers
sqr_numbers = [i*i for i in numbers]
print(sqr_numbers)

# set comperhension
s  = set ([1,1,2,3,5,4,8,9,9,])
print(s)
even={i for i in numbers if i%2== 0}
print(even)

