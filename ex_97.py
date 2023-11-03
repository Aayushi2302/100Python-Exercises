lst = []
while True:
    txt = input("Enter a string : ")
    if txt == "CLOSE":
        break
    elif txt == "SAVE":
        with open("hello.txt", "a+") as file:
            for line in lst:
                file.write(line+"\n")
            lst = []
    else:
        lst.append(txt)

