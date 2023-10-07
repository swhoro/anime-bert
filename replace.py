import sys

if len(sys.argv) < 2:
    print("no data given")
    sys.exit(1)

dataname = sys.argv[1]

content = ""
with open(dataname, "r") as f:
    content = f.read()
    content = content.replace("_", " ")

with open(dataname + ".new.txt", "w") as f:
    f.write(content)
