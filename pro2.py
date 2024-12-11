with open('./../theory/text4.txt','r') as f1:
    for line in f1:
        print (line)
    print(f1.closed)
print(f1.close())
