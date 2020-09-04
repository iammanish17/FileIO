from FileIO import FileIO

io = FileIO('input.txt', 'output.txt')
input = io.get_input
print = io.write_output

# take input from file
n = int(input())
a = list(map(int, input().split()))

x = int(input(0)) # take input from stdin

print(*[x*i for i in a], sep=", ") # write to file

print("Finished.", to_file=0) # write to stdout