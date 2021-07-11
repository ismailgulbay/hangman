import random
#Bazı random kelimeler
words = ["Bursa","Istanbul","Elma","Armut"]
def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \ 
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def getWords():
    word = random.choice(words)
    return word.upper()

word = getWords()
word_copy = "_"*len(word)
lives = 6
guessedWords=[]
guessedLetters = []
print("_ "*len(word))
while lives > 0:
    guess = input("You have {} lives and your prediction :".format(lives))
    guess = guess.capitalize()
    if guess not in guessedWords or guessedLetters:
        if len(guess) > 1:
            guessedLetters.append(guess)
        elif len(guess) == 1:
            guessedWords.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == str(guess):
                    word_copy = word_copy[0:i] + guess + word_copy[i+1:]
                    print(word_copy)
        else:
            lives -= 1
            print(word_copy)
    else:
        print("You have already guessed that letter or word.")
    if guess.upper() == word:
        print("You won! {}".format(word))
        exit()
    if "_" not in word_copy:
        print("You won! The word is {} .".format(word))
        exit()
    if lives == 0 :
        print("You lost!")
        print(display_hangman(0))
        exit()
    print(display_hangman(lives))



