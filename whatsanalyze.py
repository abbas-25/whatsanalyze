# Whatsapp Chat Analyzer

from matplotlib import pyplot as plt
from urlextract import URLExtract

print("Copy and Paste the whatsapp chat file in the same directory as this python script before proceeding!")
success = 0

while(success == 0):
    filename = input("Enter txt filename without extension: ")
    try:
        filename = filename + '.txt'
        file = open(filename, 'r')
        success = 1
    except FileNotFoundError:
        print("Chat file couldn't be found!\nMake sure it is present in the same directory\nTry re-entering the filename")
        continue
    except:
        print("There was some error in loading the file. Why don't you try again?")
        continue


def nameFinder():
    file.seek(0)
    message1 = file.readlines()[0]
    dash = message1.find('-')
    person1 = ''
    for i in range(dash + 2, len(message1)):
        if message1[i] == ':':
            break
        else:
            person1 += message1[i]

    person2 = ''
    file.seek(0)
    for i in range(1, len(file.readlines())):
        file.seek(0)
        message2 = file.readlines()[i]
        dash = message2.find('-')
        tempPerson2 = ''
        for j in range(dash + 2, len(message2)):
            if message2[j] == ':':
                break
            else:
                tempPerson2 += message2[j]
        if(tempPerson2 == person1):
            i = i + 1
        else:
            person2 = tempPerson2
            break
    return [person1, person2]


monthCountDict = {
    'Jan': 0,
    'Feb': 0,
    'Mar': 0,
    'Apr': 0,
    'May': 0,
    'Jun': 0,
    'Jul': 0,
    'Aug': 0,
    'Sep': 0,
    'Oct': 0,
    'Nov': 0,
    'Dec': 0
}


def monthCalculator(monthNumber):
    numberToMonthList = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May',
                         'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    monthName = numberToMonthList[monthNumber]
    monthCountDict[monthName] += 1

    return monthCountDict


extractor = URLExtract()


def urlChecker(message):
    links = []

    links = extractor.find_urls(message)
    if len(links) == 0:
        return False
    else:
        return True


def imageChecker(message):
    if '<Media omitted>' in message or '(file attached)' in message:
        return True
    else:
        return False


def createEmojiFrequencyDict():
    emojiFrequencyDict = emoji_pack
    for emoji in emojiFrequencyDict:
        emojiFrequencyDict[emoji] = 0

# def emojiChecker(message):
#    for emoji in emoji_pack:
#        if emoji in message:
#            emojiCountTemp = emojiCount + message.count(emoji)


def messageAnalyzer():
    person1Count = 0
    person2Count = 0
    monthNumber = 0
    imageCount = 0
    linkCount = 0
    totalWords = 0
    emojiCount = 0
    file.seek(0)
    for line in file:
        try:
            monthNumber = int(line[3:5])
            # error: not a separate/new message, move to except
            if imageChecker(line) == True:
                imageCount += 1

            if urlChecker(line) == True:
                linkCount += 1

            # if emojiChecker(line) == True:
            #    emojiCount += 1

            if person1 in line:
                person1Count += 1
            elif person2 in line:
                person2Count += 1

            perMonthMessageCountDict = monthCalculator(monthNumber)
        except:
            continue

    return {'person1Count': person1Count, 'person2Count': person2Count,
            'perMonthMessageCountDict': perMonthMessageCountDict, 'imageCount': imageCount,
            'linkCount': linkCount}


def plotMonthFrequency(monthFrequency):
    plt.bar(monthFrequency.keys(), monthFrequency.values())
    plt.title('Month-wise Analysis')
    plt.xlabel("Month")
    plt.ylabel("Number of message(s)")
    plt.show()


def plotMessageCount(person1Count, person2Count):
    plt.bar(person1, person1Count)
    plt.bar(person2, person2Count)
    plt.title(person1 + ' vs ' + person2)
    plt.show()


person1 = nameFinder()[0]
person2 = nameFinder()[1]
messageAnalysisDict = messageAnalyzer()

print("Total number of messages from "
      + str(person1) + ": " + str(messageAnalysisDict['person1Count']))
print("Total number of messages from "
      + str(person2) + ": " + str(messageAnalysisDict['person2Count']))

print("Total number of messages:"
      + str(messageAnalysisDict['person1Count'] + messageAnalysisDict['person2Count']))

print("Total number of images exchanged:"
      + str(messageAnalysisDict['imageCount']))

print("Total number of links exchanged:"
      + str(messageAnalysisDict['linkCount']))

# print("Total number of emojis exchanged:" +
#      str(messageAnalysisDict['emojiCount']))

# createEmojiFrequencyDict()

plotMonthFrequency(messageAnalysisDict['perMonthMessageCountDict'])
plotMessageCount(
    messageAnalysisDict['person1Count'], messageAnalysisDict['person2Count'])
