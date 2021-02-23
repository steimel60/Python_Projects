import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old.
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    pattern = re.compile(r'[A-Z]\w+')
    matches = pattern.finditer(simple_string)
    names = []

    for match in matches:
        names.append(match.group(0))

    return names
