# hmmm what am I going to type for reading from a file?
# Could we use import? No because import only works with reading Python code.
# import example:
from x00_python_code import my_text
print(my_text)

f = open('x00_text_file.txt', 'r') # filename to be opened and 'r' for read access
print(f.read())

f = open('x00_text_file.txt', 'r')
print(f.read(5))   # 5 argument will allow reading the first 5 charachters only

f = open('x00_text_file.txt', 'r')
print(f.readline())   # This will read the first line
print(f.readline())   # This will read the second line

f = open("x00_text_file.txt", "r")
for x in f:
  print(x)

# It is good practice to close a file after we finished working with it.
# Only a cloased file is available for access by other users.
f.close()

