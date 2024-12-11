with open('./textile2.txt','w') as f1:                  #it overwrite the existing with given one
    print(f1.write("you cant decide your life with someone god decide it for you.. "))
    

with open('./textile2.txt','a') as f2:                  #it adds at end because we use 'a' mode
    print(f2.write("hello"))
    print(f2.write("['bro i dont care']"))  

with open('./textile2.txt','a') as f3:
    print(f3.writelines("if you trouble the trouble the trouble will trouble i am not the trouble i am the trueth."))
    print(f3.writelines(['jai balaya','dabididebide']))
    f3.seek(2000)
    print(f3.tell())
