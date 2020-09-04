import sys

class FileIO:
    def __init__(self, input_file, output_file = None):
        self.lines = [line for line in open(input_file, 'r')][::-1]
        self.output_file = output_file
        self.clear_file()

    def clear_file(self):
        if self.output_file:
            with open(self.output_file, 'w') as f:
                f.close()

    def get_input(self, from_file=1):
        """Get input from file or from stdin."""
        return self.lines.pop() if from_file else sys.stdin.readline()

    def write_output(self, *content, to_file=1, sep=" "):
        """Write output to file or to stdout."""
        content = sep.join(str(k) for k in content) + "\n"
        if self.output_file and to_file:
            with open(self.output_file, 'a') as f:
                f.write(content)
                f.close()
        else:
            sys.stdout.write(content)