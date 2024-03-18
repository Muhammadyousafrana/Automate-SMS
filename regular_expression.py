import re

pattern = re.compile('you doing this is so crazy')
string = 'what the hell are you doing this is so crazy'

a = pattern.search(string)
b = pattern.fullmatch(string)
c = pattern.findall(string)
d = pattern.search(string, 16)
print(d)
print(c)
print(b)
print(a.span())
