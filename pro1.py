file_name=open('./../theory/text4.txt')
# for line in file_name:
    # print(line)
print(file_name.name)               #attributes of filehandling.
print(file_name.mode)
print(file_name.readable())
print(file_name.writable())
print(file_name.closed)
print(file_name.close)
print(file_name.closed)

file_name.close()
print(file_name.closed)
