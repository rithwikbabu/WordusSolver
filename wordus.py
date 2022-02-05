import requests as req
class Wordus:

    def __init__(self, yellowList=[], greenList=[], redList=[]):
        self.yellowList = yellowList
        self.greenList = greenList
        self.redList = redList
        self.res = req.get("https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt").text.splitlines()

    def nextMove(self, word):
        temp = input("In what are position are the green letters?\n")
        if len(temp) == 5:
            return False
        for letter in temp:
            if letter != "0":
                index = int(letter)-1
                self.greenList.append([word[index], index])
        temp = input("In what are position are the yellow letters?\n")
        for letter in temp:
            if letter != "0":
                index = int(letter)-1
                self.yellowList.append([word[index], index])
        temp = input("In what are position are the red letters?\n")
        for letter in temp:
            if letter != "0":
                index = int(letter)-1
                self.redList.append(word[int(letter)-1])
        self.__getWords()
        return True

    def __getWords(self):
        temp = list(self.res)
        for x in self.yellowList:
            res = list(temp)
            for y in res:
                if x[0] not in y:
                    temp.remove(y)
                if x[0] in y[x[1]]:
                    temp.remove(y)

        for x in self.greenList:
            res = list(temp)
            for y in res:
                if x[0] != y[x[1]]:
                    temp.remove(y)

        for x in self.redList:
            res = list(temp)
            for y in res:
                if x in y:
                    temp.remove(y)
        print(temp)
    
