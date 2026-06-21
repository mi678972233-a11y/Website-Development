import os
print("Sciences Notes")
with open("Science-notes.txt", "r") as file:
    content = file.read()
    print(content)
    print("\n Maths Notes Word Count: ",)
with open("Maths-notes.txt", "r") as file:
        for line in file:
            words = line.split()
            word_count = len(words)
            print("Line:", line.strip())
            print("Word Count:", len(words))
            if not os.path.exists("all - notes.txt"):
                with open("Science-notes.txt", "r") as f1:
                    science = f1.read()
                with open("Maths-notes.txt", "r") as f2:
                    maths = f2.read()
                with open("all - notes.txt", "w") as f3:
                    f3.write(science + "\n" + maths)
                    print("\n Files Merged Successfully.")
                    print("\n All Notes.txt already exists.")
            if os.path.exists("all - notes.txt"):
                        print("\n All Notes.txt deleted.")
            else:
                        print("File not found.")    