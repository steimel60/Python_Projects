import re
import os

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
900-555-4321
800.555.1234

Mr. Shafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

#here = os.path.dirname(os.path.abspath(__file__))
#filename = os.path.join(here, 'data.txt')

#with open(filename, 'r') as f:
#    contents = f.read()
#    matches = pattern.finditer(contents)

#    for match in matches:
#        print(match)
