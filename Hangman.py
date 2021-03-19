import random

print("H A N G M A N")

li_of_words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(li_of_words)
new_word = []
for char in word:
    new_word.append('-')

failures = 0
while failures <= 7:
    print()
    print(str.join('', new_word))
    guess = input('Input a letter: ')
    guessed = False
    if guess in new_word:
        print('No improvements')
        failures += 1

    for ind, char in enumerate(word):
        if char == guess:
            guessed = True
            new_word[ind] = char

    if '-' not in new_word:
        print('You guessed the word! \nYou survived!')
        break

    if not guessed:
        print("That letter doesn't appear in the word")
        failures += 1

else:
    print('You lost!')


