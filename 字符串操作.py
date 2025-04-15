text = "Hello World!"
numeric_text = "12345"
lowercase_text = "hello"
uppercase_text = "HELLO"

# str.lower()
print(text.lower())

# str.upper()
print(text.upper())

# str.islower()
print(lowercase_text.islower())
print(uppercase_text.islower())

# str.isnumeric()
print(text.isnumeric())
print(numeric_text.isnumeric())

# str.count(sub)
print(text.count('l'))
print(text.count('o'))

# str.replace(old, new)
print(text.replace('World', 'Python'))
print(numeric_text.replace('45', '21'))

# str.center(width, fillchar)
print(text.center(50, '*'))
print(text.center(1, '#'))

# str.find(sub)
print(text.find('o'))
print(text.find('a'))

# str.strip(chars)
print(numeric_text.strip('45'))

# str.split(sep)
print(text.split(' '))

# str.join(iter)
print(' '.join(text.split(' ')))