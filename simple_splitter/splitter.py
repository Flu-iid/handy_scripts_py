# /usr/bin/python

from sys import argv

name, path, marks, *extra = argv

print("Warnning! : extra inputs given\n" if extra else "", end="")

result = path.translate(str.maketrans(marks, "\n" * len(marks)))

print(result)
