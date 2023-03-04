colors = ['red', 'green', 'blue']

print(colors)
print(f"List have {len(colors)} colors")
print(f"First element is {colors[0]} and last is {colors[-1]}")
print(f"La lista colores {'TIENE' if 'green' in colors else 'NO TIENE'} el color verde")
print(f"La lista colores {'TIENE' if 'violet' in colors else 'NO TIENE'} el color violeta")

print('Adding violet color...')
colors.append('violet')
print(f"La lista colores {'TIENE' if 'violet' in colors else 'NO TIENE'} el color violeta")


print('Adding some colors...')
colors.extend(['yellow', 'orange', 'purple'])
print(f"Colors added! {colors}")


# Insert into position
colors.insert(2, 'brown')
print(colors)

# Remove elements from array
# colors.pop()
# colors.remove('pink')
# colors.clear()

# Ordenar
colors.sort()
colors.sort(reverse=True)
