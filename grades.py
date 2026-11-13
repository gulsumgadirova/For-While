students = [("Aysel", 95), ("Murad", 72), ("Leyla", 84), ("Elvin", 48), ("Nigar", 63)]

for name, grade in students:
    if grade >= 91:
        result = "A"
    elif grade >= 81:
        result = "B"
    elif grade >= 71:
        result = "C"
    elif grade >= 61:
        result = "D"
    elif grade >= 51:
        result = "E"
    else:
        result = "F"

    print (name + ":", grade, "->", result)
