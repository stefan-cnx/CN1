f = open('x02-a-file-created-by-python.txt', 'w')
f.write('This is the first line in the very new file\n')
f.write('This is the second line in the new file\n')
f.close()

input('Script is paused for you to check your file browser for the new file!')

f = open('x02-a-file-created-by-python.txt', 'a')
f.write('This is the third line in the new file\n')
f.close()

f = open('x02-a-file-created-by-python.txt', 'r')
print(f.read())
f.close()
