with open('./textfile1.txt','r') as f1:                     #read
    print(f1.read(6))       #first six cherecters
    print(f1.read(10))      #after 10 cherecters


with open('./textfile1.txt','r') as f2:                     #readline
    print(f2.readline())
    print(f2.readline())
    print(f2.readline(10))


with open('./textfile1.txt','r') as f3:                     #readlines
    print(f3.readlines())
    