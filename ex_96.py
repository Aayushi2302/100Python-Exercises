lst = []
while True:
    txt = input("Enter a string : ")
    if txt == "CLOSE":
        break
    lst.append(txt)

with open("demo.txt", "a+") as file:
    for line in lst:
        file.write(line+"\n")