import random

from PyDictionary import PyDictionary

wordData = PyDictionary ()


# This function contains the dictionary of words
def load_words():
    with open ('.\\words\\words.txt') as word_file:
        valid_words = set (word_file.read ().split ())
    return valid_words


eng_words = load_words ()

# A list of letter that will be randomized for the user to guess a word
alphabets = ["A", "B", "C", "D", "E", "F", "G", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
             "X", "Y", "Z"]

# a list positive comments for every word guessed correctly
goodExpression = ["Amazing!!!", "Awesome!!!", "Great Job!!!", "Superb !!!",
                  "You're Too Good!!!", "Scholar!!!"]

while True:
    ChallengeLetter = random.choice (alphabets)
    print (f'{ChallengeLetter}')
    # score = 0
    # for item in score:
    #     score += 1
    #     print(f'Score:{score}')

    gExpression = random.choice (goodExpression)

    userData = str (input (f' Enter a word that starts with the letter {ChallengeLetter}:  ')).lower ().upper ()
    Score = 0
    if userData.startswith (ChallengeLetter) and userData in eng_words:
        # Score += 1
        print (gExpression)
        # for i in Score:
        #     Score += 1
        #     print(f'Score:{Score}')
        # # while gExpression is True:
        # #     score += 1
        # #     print(f'Score:{score}')
        # # else:
        # #     score -= 1
        # #     print(f'Score:{score}')
        #
        # print(f'Score:{score}')
    # elif userData.startswith(ChallengeLetter) and userData in eng_words

    else:
        print (f'sorry cannot find {userData} in our wordlist !!!')
