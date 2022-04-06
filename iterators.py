a = ["hey", "bro", "you'r", "awesome"]
for i in a:
    print(i)

print(dir(a))
itr= iter(a) # using iter method
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


class RemoteControl():
    def __init__(self):
        self.channels = ["HBO", "CNN", "abc", "espn"]
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        
        return self.channels[self.index]
    
r = RemoteControl()
itr= iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

