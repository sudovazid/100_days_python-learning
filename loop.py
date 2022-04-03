exp = [2340, 2500, 2100, 3100, 2980]
# total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
# Using for loop
total = 0 
for item in exp:
    total = total + item
print(total)

# using range function

for i in range(1, 11):
    print(i)

for i in range(len(exp)):
    print('Month: ', (i+1), 'Expense: ', exp[i])
    total = total + exp[i]

print('Total expenses is: ', total) 

# searching key using for loop and break

key_location="chair"
locations = ['garage', 'living room', "chair", "closet"]
for i in locations:
    if i==key_location:
        print("key is found in ", i)
        break
    else:
        print("Key is not found in ", i)

# print squre of 1 to 5  except  even number

for  i in range(1,6):
    if i%2==0:
        continue
    print(i*i)


# using while loop

i=1
while i<=5:
    print(i)
    i = i + 1