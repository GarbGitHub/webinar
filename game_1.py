import random

words_bank = [
   'монитор', 'бензин', 'инопланетянин',
   'самолет', 'библиотека', 'шайба',
   'олимпиада', 'словарь', 'береза', 'журнал'
]

secret_word = random.choice(words_bank)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_counter = 0
while True:
   letter = input('введите ОДНУ русскую букву:\n')
   if len(letter) != 1:
       continue

   if letter in secret_word:
       for idx, symbol in enumerate(secret_word):  # (idx, item)
           if symbol == letter:
               gamer_word[idx] = letter
       if '*' not in gamer_word:
           print('вы выиграли')
           break
   else:
       errors_counter += 1
       print('ошибок допущено:', errors_counter)
       if errors_counter == 8:
           print('вы проиграли')
           break

   print(''.join(gamer_word))

# os.walk()

# immutable VS mutable
# immutable -> object does not support item assignment
# str, float, int, bool, tuple
# mutable -> list, set, dict

