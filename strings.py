myStr = "Hello world!"

# Dir muestra qué métodos tiene cierto tipo de dato
options  = dir(myStr)
print(options)

print(myStr.upper())
print(myStr.lower())
print(myStr.split(' ')[0])
myStr = myStr.replace('!', '||')
print(myStr)
print(myStr.count('l'))
start_with_hello = myStr.startswith('Hello')
print(start_with_hello)
# Index
print(myStr.find('world!'))
print(myStr.index('w'))

name = "Sebastian"

print("Mi nombre es " + name)
print(f"Mi nombre es {name}")
