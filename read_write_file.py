# Writing to file
f=open("C:\\data\\funny.txt","a")
f.write("\nJavaScript programming")
f.close()

# Reading file
f=open("C:\\data\\funny.txt","r")
print(f.read())
f.close()

f=open("C:\\data\\funny.txt","r")
for line in f:
    print(line)
f.close()

f=open("C:\\data\\funny.txt","r")
f_out=open("C:\\data\\funny_wc.txt","w")
for line in f:
    tokens = line.split(' ')
    print(len(tokens))
for line in f:
    tokens = line.split(' ')
    f_out.write(line+" wordcount:"+str(len(tokens))+line)

f.close()
f_out.close()