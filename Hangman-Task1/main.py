import random
from word import word_list
score=[]
sc=[]
def get_word():
    word=random.choice(word_list)
    return word.upper()


def play(word):

    word_completion="_" *len(word)
    guessed=False
    guessed_letters=[]
    guessed_words = []
    tries=6
    pts=0
    print("Lets Play HANGMAN!")
    print("The Theme For The Game Is FRUITS")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries>0:
        guess=input("Please guess a letter:").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter",guess)
            elif guess not in word:
                print(guess,"is not in the word.")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("Good Job",guess,"is in the word!")
                pts+=1
                # print(pts)
                score.append(pts)
                guessed_letters.append(guess)
                word_as_list=list(word_completion)
                indices=[i for i,letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion="".join(word_as_list)
                if "_" not in word_completion:
                    guessed=True



        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word",guess)
            elif guess!=word:
                print(guess,"is not the word.")
                tries-=1
                guessed_words.append(guess)
            else:
                guessed=True
                pts+=1
                score.append(pts)
                word_completion=word
        else:
            print("not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print(f"Congrats,you guessed the word! you win {score[-1]} points")
        sc.append(score[-1])

    else:
        print(f"sorry, you ran out of tries.The word was {word} maybe next time!Your Score is {score[-1]} points")
        sc.append(score[-1])

def display_hangman(tries):
    stages=["""
                ---------
                |       |
                |       o
                |      \\|/
                |       |
                |      / \\
                -
            """,
            """
                ---------
                |       |
                |       o
                |      \\|/
                |       |
                |      / 
                -
            """,
            """
                ---------
                |       |
                |       o
                |      \\|/
                |       |
                |      
                -
            """,
            """
                ---------
                |       |
                |       o
                |      \\|
                |       |
                |      
                -
            """,
            """
                ---------
                |       |
                |       o
                |       |
                |       |
                |      
                -
            """,
            """
                ---------
                |       |
                |       o
                |        
                |       
                |      
                -
            """,
            """
                ---------
                |       |
                |       
                |      
                |       
                |      
                -
            """
    ]
    return stages[tries]

def main():

    word=get_word()
    play(word)
    while input("play again?(Y/N)").upper()=="Y":
        word=get_word()
        play(word)
        print(f"TOTAL SCORE : {sum(sc)}")
if __name__ == "__main__":
    main()


