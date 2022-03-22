f = open("file_with_400000_lines.txt", "w")

for _ in range(400000):
  f.write("a" * 100 + "\n")

f.close()