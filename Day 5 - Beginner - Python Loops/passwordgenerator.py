import random

letters = input('how many letters would you like in your password ? : ')
symbols = input('how many symbols you like? : ')
numbers = input('how many numbers you like? : ')

ltr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nbr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sym = ['!', '@', '#', '$', '%', '&', '*', '+', '-', '=', '?']

picked =[]
for letter in range(int(letters)):
    picked.append(random.choice(ltr))

for n in range(int(numbers)):
    picked.append(random.choice(nbr))

for s in range(int(symbols)):
    picked.append(random.choice(sym))
    
print(f'''
      password : {picked}
      ''')

random.shuffle(picked)
my_password = ''.join(str(pick) for pick in picked)
print(f'''
      password : {my_password}
      ''')

