import sys

if len(sys.argv) != 2:
	print("no .bin file specified")
	exit(1)
if sys.argv[1][-4:] != ".bin":
    print("file isn't a .bin file")
    exit(1)

file = sys.argv[1]

header = b"\x0f\x00\xff\x00\x00\x009`\xff\xff\xff\xff\xff\xff\xff\xff"
with open(file, "rb") as f:
    content = f.read()

content = content[:16] + header + content[32:]

with open(file, "wb") as f:
    f.write(content)
