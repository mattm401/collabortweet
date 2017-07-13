#!/usr/bin/python

import sqlite3
import sys
import json
import codecs
import itertools
import random

taskDescPath = sys.argv[1]
sqlitePath = sys.argv[2]
tweetPath = sys.argv[3]

pairCount = None
if (len(sys.argv) > 4):
    pairCount = int(sys.argv[4])

taskDesc = {}
with codecs.open(taskDescPath, "r", "utf8") as inFile:
    taskDesc = json.load(inFile)

print taskDesc

tweetList = []


# Get the contents of this tweet
def readTweet(tweetObj):
    tweetText = tweetObj["html"]
    tweetId = tweetObj["VideoID"]
    return (tweetText, tweetId)


with codecs.open(tweetPath, "r", "utf8") as inFile:
    for line in inFile:
        tweet = json.loads(line)

        (tweetText, tweetId) = readTweet(tweet)

        if (tweetText == None):
            print "Skipping:", line
            continue

        tweetList.append((tweetText, tweetId))

# Open the sqlite3 file
conn = sqlite3.connect(sqlitePath)
c = conn.cursor()

c.execute("INSERT INTO tasks (taskName, question, taskType) VALUES (:name,:question,:type)",
          taskDesc)
taskId = c.lastrowid
print "Task ID:", taskId

elementList = map(lambda x: (taskId, x[0], x[1]), tweetList)
elementIds = []
for elTup in elementList:
    c.execute('INSERT INTO elements (taskId, elementText, externalId) VALUES (?,?,?)',
              elTup)
    elId = c.lastrowid
    elementIds.append(elId)

print "Element Count:", len(elementIds)

# Only create pairs if the task type == 1
if (taskDesc["type"] == 1):
    # Create the pairs
    pairList = None

    # If we didn't specify a number of pairs, find all
    if (pairCount == None):
        pairList = itertools.combinations(elementIds, 2)

    else:  # Otherwise, randomly select k pairs
        pairAccum = set()

        for eIndex in range(len(elementIds)):
            eId = elementIds[eIndex]
            startIndex = max(0, eIndex - 1)
            others = elementIds[:startIndex] + elementIds[eIndex + 1:]

            # Put the pair in canonical order to avoid duplicates
            newPairs = set(map(lambda x: (min(eId, x), max(eId, x)),
                               random.sample(others, pairCount)))

            pairAccum = pairAccum.union(newPairs)

        pairList = list(pairAccum)

    pairList = [(taskId, x[0], x[1]) for x in pairList]
    print "Pair Count:", len(pairList)

    c.executemany('INSERT INTO pairs (taskId, leftElement, rightElement) VALUES (?,?,?)',
                  pairList)

# If we are dealing with a labeling task (type == 2), insert the labels
elif (taskDesc["type"] == 2):

    print "Insert labels..."
    labelList = map(lambda x: {"taskId": taskId, "labelText": x}, taskDesc["labels"])
    print labelList

    c.executemany('INSERT INTO labels (taskId, labelText) VALUES (:taskId,:labelText)',
                  labelList)

# Otherwise, we have an invalid task type
else:
    print "ERROR! Task type [" + taskDesc["type"] + "] is not valid!"

conn.commit()
conn.close()
