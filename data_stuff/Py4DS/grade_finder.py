import re



def grades():
    with open("grades.txt", "r") as file:
        grades = file.read()
    # YOUR CODE HERE
    pattern = re.compile(r'([A-Z-]\w+\s[A-Z]\w+):\s(B)')
    matches = pattern.finditer(grades)
    names = []

    for match in matches:
        names.append(match.group(1))
    print(len(names))
    return names

grades()
