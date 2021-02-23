import re

with open("ass1logdata.txt", "r") as file:
    logdata = file.read()

pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)\s-\s([a-z0-9-]+)\s\[(\d{2}/[A-Za-z]+/\d{4}:\d{2}:\d{2}:\d{2}\s-\d{4})\]\s"([A-Z]+\s[\S]+\s[A-Z]+/\d\.\d)"')
matches = pattern.finditer(logdata)
logs = []

for match in matches:
    #print(match.group(4))
    item_dict = {'host' : match.group(1),
                'user_name' : match.group(2),
                'time' : match.group(3),
                'request' : match.group(4)}

    logs.append(item_dict)
