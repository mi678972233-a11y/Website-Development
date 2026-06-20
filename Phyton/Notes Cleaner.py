n=int(input("How many characters to preview? "))
file = open("My Notes.txt", "r")
content = file.read(n)
file.close()
print()
file = open("My Notes.txt", "r")
lines = file.readlines()
file.close()
print("Total lines in the file: ", len(lines))
for i in range(len(lines)):
    print(i+1, "->", lines[i].strip())
print()
word = input("Skips Lines Starting With: Hi")
file = open("My Notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    else:
        print(line.strip())
file.close()
print()
file = open("My Notes.txt", "r")
lines = file.readlines()
file.close()
out = open("Odd - lines.txt", "w")
for i in range(0, len(lines), 2):
    if i % 2 == 0:
        out.write(lines[i])
out.close()
print("Odd lines saved to Odd - lines.txt")