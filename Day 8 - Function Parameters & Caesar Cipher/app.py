
ltr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']





def encode(word, code_nm):

    coded = ''
    for char in word:
        pos = ltr.index(char)
        new_pos = pos + code_nm
        if new_pos > len(ltr):
            new_pos -= len(ltr)
        new_char = ltr[new_pos]
        coded += new_char
        print(coded)

    return coded


def decode(word, code_num):
    old_word = ''
    for chat in word:
        position = ltr.index(chat)
        old_pos = position - code_nm
        old_ltr = ltr[old_pos]
        old_word += old_ltr
        print(old_word)


print('welcome to ceasar ciphir encryption program .')
type_code = input(
    'type "encode" to encrytpe n type "decode" to decrypt : ')
word = input('write the word you want to code or decode : ').lower()
code_nm = int(input('write your coding number and remember it :'))
if type_code == 'encode':
    encode(word, code_nm)
elif type_code == 'decode':
    decode(word, code_nm)
