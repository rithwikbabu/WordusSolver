from wordus import Wordus

if __name__ == "__main__":
    wordgame = Wordus()

    loop = True
    while loop:
        temp = input("What is your Guess?\n")
        loop = wordgame.nextMove(temp)
    else:
        print("Solved!")
