"""
When loading from a file in Pyzo you have to run the script from the file
system. If you don't do that, it won't be able to find your file.

From the Run menu choose "Run File as Script" or hit CTRL-SHIFT-E

Sam Scott, Mohawk College, 2021
"""
def file_input(filename):
    """Loads each line of the file into a list and returns it."""
    lines = []
    with open(filename) as file: # opens the file and assigns it to a variable
        for line in file:
            lines.append(line.strip()) # the strip method removes extra whitespace
    return lines

print(file_input("questions.txt"))