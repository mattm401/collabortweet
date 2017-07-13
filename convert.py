import csv
import json






# Open the CSV
f = open('./scraper.csv', 'rb')
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader(f, fieldnames=("VideoID", "Title", "Description"))

writer = csv.DictWriter(f, fieldnames=("VideoID", "Title", "Description"))
# Parse the CSV into JSON

a = []
headerRow = False
for row in reader:
    if (headerRow == False):
        headerRow = True
        continue
    #json.wite(<iframe ... href=\""+row["Video"]+"\">")
    src = ' src="http://www.youtube.com/embed/' + row['VideoID']

    whole = '<iframe ' + src + "\"" + ' width="560" height="315" frameborder="0" allowfullscreen></iframe>'

    title = row['Title']

    entire = '<h2>' + title + '</h2>' + '<br><br>' + whole


    second = "<br><br><p>" + row['Description'] + "</p>"

    actualentire = { "VideoID" : row['VideoID'], "html": entire+second}
    a.append(actualentire)
print a

    #writer.write(actualentire)
#writer.writerow(outside)


#out = json.dumps(a)
#print "JSON parsed!"
# Save the JSON
#f = open('./tweetSample.json', 'w')
#f.write(out)


with open('tweetSample.json', 'wb') as outfile:
    json.dump(a, outfile)




