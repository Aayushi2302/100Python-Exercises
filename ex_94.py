# EX 94
with open("urls.txt", "r") as file:
        content = file.readlines()
    
with open("urls.txt", "w") as file:
    for line in content:
        line = line.replace("s", "", 1)
        line = line[:5] + "/" + line[5:]
        file.write(line)