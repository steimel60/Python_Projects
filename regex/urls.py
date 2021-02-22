import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'(?<=[https]:\/\/)([A-Za-z0-9.]*)')

#subbed_urls = pattern.sub(r'\2\3', urls)

#print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match)
