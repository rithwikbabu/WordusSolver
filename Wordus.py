# Developed to be run in a notebook environment
# Run once
import requests as req
yellowList=[]
greenList=[]
redList=[]

# Run until desired outcome
Word = "sound"
yellowLetters = "24"
greenLetters = "1"
redLetters = "35"

for x in yellowLetters:
  if x != "0":
    index = int(x)-1
    yellowList.append([Word[index], index])
for x in greenLetters:
  if x != "0":
    index = int(x)-1
    greenList.append([Word[index], index])
for x in redLetters:
  if x != "0":
    redList.append(Word[int(x)-1])

url = "https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"
res = req.get(url)
res = res.text.splitlines()

temp = list(res)
for x in yellowList:
  res = list(temp)
  for y in res:
    if x[0] not in y:
      temp.remove(y)
    if x[0] in y[x[1]]:
      temp.remove(y)

for x in greenList:
  res = list(temp)
  for y in res:
    if x[0] != y[x[1]]:
      temp.remove(y)

for x in redList:
  res = list(temp)
  for y in res:
    if x in y:
      temp.remove(y)
print(temp)
