import random


word_list = ['baboon', 'camel', 'kako']

picked_word = random.choice(word_list)


word = []
lives = 5
for char in picked_word:
    word += '_'

while ('_' in word) and lives > 0:
    letter = input(f'guess a latter inclided in {picked_word}: ').lower()
    if letter in picked_word:
        for i in range(len(picked_word)):
            if picked_word[i] == letter:
                word[i] = letter
    else:
        lives -= 1
        print(f'baad u just lost a life brother left {lives} atemptes')
    print(word)

if lives > 0:
    print('you win')
else:
    print('try again later brother')
