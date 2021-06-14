#fname = "hello-world.txt"
#file_object = open(fname, "w")
#file_object.write("Hello World")
#file_object.close()
# creates a .txt file that has hello world in it 

#with open(fname, "w") as file_object:
#    file_object.write("Hello World Again")

fname = 'hello-world.txt'
with open (fname, 'r') as f:
    print(f.read())