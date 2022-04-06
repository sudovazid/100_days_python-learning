# define set
basket={"apple", "orange", "mango", "orange"}
print(type(basket))
print(basket)

a=set()
a.add(1)
print(a)

numbers = [1,2,3,4,5,4,3,2,]
unique_numbers=set(numbers)
unique_numbers.add(6)
print(unique_numbers)
# frozen set
fs = frozenset(numbers)
print(fs)
fs.add(8)