# FileIO
 
A Python class to manage input/output from files and stdin/stdout easily and simultaneously if needed.

# Usage

Import the class and re-define the `input` and `print` functions.

```
from FileIO import FileIO
io = FileIO('input.txt', 'output.txt')

input = io.get_input
print = io.write_output
```

Use them to get the input or write the output to file/stdout.

```
# take input from file
n = int(input())
a = list(map(int, input().split()))

x = int(input(0)) # take input from stdin

print(*[x*i for i in a], sep=", ") # write to file

print("Finished.", to_file=0) # write to stdout
```
