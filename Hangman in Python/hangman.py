import random
from words import word_list

def get_word() :
    word = random.choice(word_list)
    return word.upper()

def play(word) :
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 10
    print("Bienvenue au jeu du Pendu !")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0 :
        guess = input("Choississez un mot ou une lettre : ").upper()
        if len(guess) == 1 and guess.isalpha() :
            if guess in guessed_letters :
                print("Vous avez déjà soumis la lettre", guess)
            elif guess not in word :
                print(guess, "n'est pas le bon mot")
                tries -= 1
                guessed_letters.append(guess)
            else :
                print("Bien joué !", guess, "est le bon mot !")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices :
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion :
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha() :
            if guess in guessed_words :
                print("Vous avez déjà soumis le mot", guess)
            elif guess != word :
                print(guess, "n'est pas le bon mot")
                tries -= 1
                guessed_words.append(guess)
            else :
                guessed = True
                word_completion = word
        else :
            print("Ce n'est pas la bonne réponse")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed :
        print("Bravo ! Vous avez justement deviné le mot du jeu !")
    else:
        print("Désolé, vous avez utilisé tous vos essais" + word + "Réessayez la prochaine fois !")

def display_hangman(tries) :
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
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

def main() :
    word = get_word()
    play(word)
    while input("Souhaitez-vous rejouer ? O/N ").upper() == "O" :
        word = get_word()
        play(word)

if __name__ == "__main__" :
    main()
