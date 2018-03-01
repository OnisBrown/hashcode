filename = "inputs/a_example.in"
file = open(filename,"r")
lines = sum(1 for line in file)
count = 0
out = file.read()
print(out)
print(lines)

while(count <= lines - 1):
    file.readline(count)
    count += 1
    
file.close()
