import re


def getCommit(commit):
    return re.sub('[!+0?]', '', commit)


sample1 = "0??+0+!!someCommIdhsSt"
print(getCommit(sample1))
