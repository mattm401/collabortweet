import csv
import json
import decimal
import codecs






# Open the CSV
f = open('./scraper.csv', 'rb')
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader(f, fieldnames=("VideoID", "Title", "Description" , "Author"))

writer = csv.DictWriter(f, fieldnames=("VideoID", "Title", "Description", "Author"))
# Parse the CSV into JSON

a = []
headerRow = False
with open('tweetSample.json', 'wb') as outfile:

    for row in reader:
        if (headerRow == False):
            headerRow = True
            continue
    #json.wite(<iframe ... href=\""+row["Video"]+"\">")
        src = ' src="http://www.youtube.com/embed/' + row['VideoID']

        whole = '<div style="max-height:300px;"><iframe style=\"float:left; padding-right:12px; padding-left:8px;\"' + src + "\"" + ' width="560" height="315" frameborder="0" allowfullscreen></iframe>' + "<br><h4 style=\"position: relative;top: 320px;right: 560px;\">Author:" + row['Author']  + "</h4>"+  "</div>"

        title = row['Title']

        entire = '<h2 style=\"text-align:center\">' + title + '</h2>' + '<br><br>' + whole


        second = "<div style=\"float: right;width:550px; height:350px;position: relative; top: -20px;left: -300px;overflow-y: scroll;\"><h3>Description</h3><p style=\"word-break: break-all; white-space: normal; margin-right:13px;\">"  + row['Description'] + "</p></div>"

        actualentire = { "VideoID" : row['VideoID'], "html": entire+second}
        #a.append(actualentire)
        outfile.write(json.dumps(actualentire) + "\n")
    print a

    #writer.write(actualentire)
#writer.writerow(outside)


#out = json.dumps(a)
#print "JSON parsed!"
# Save the JSON
#f = open('./tweetSample.json', 'w')
#f.write(out)



    #json.dump(a, outfile)




