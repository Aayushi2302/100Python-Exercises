planet_input = input("Enter a string of planets separated by , : ")
planet_input = planet_input.split(",")
print(planet_input)
with open("planets.txt", "a+") as file:
    for line in planet_input:
        file.write(line+"\n")