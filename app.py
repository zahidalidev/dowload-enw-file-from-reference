reference_file = open("references.txt", encoding="utf8")
f = open("new.txt", "a",  encoding="utf8")

for line in reference_file:
    reference_file.readline()
    f.write(f', "{reference_file.readline()}"')

f.close()
