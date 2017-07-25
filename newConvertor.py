import csv
import json
import decimal
import codecs






# Open the CSV
f = open('./IRR1_189_Exported.csv', 'rb')
# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader(f, fieldnames=("externalId", "elementId", "labelId" , "userId"))

firstOrSecond = "first"

with open('converted.json', 'wb') as outfile:
    firstPart = ""
    secondPart = ""
    elementId = 1
    for row in reader:
        productReview2 = "Product Review (2)" + ":0"
        productReview7 = "Product Review (7)" + ":0"
        newsCoverage2 = "News Coverage (2)" + ":0"
        newsCoverage7 = "News Coverage (7)" + ":0"
        unboxing2 = "Unboxing (2)"+ ":0"
        unboxing7 = "Unboxing (7)"+ ":0"
        demonstration2 = "Demonstration (2)"+ ":0"
        demonstration7 = "Demonstration (7)"+ ":0"
        ad2 = "Advertisement (2)"+ ":0"
        ad7 = "Advertisement (7)"+ ":0"
        unstruct2 = "Unstructured Use (2)"+ ":0"
        unstruct7 = "Unstructured Use (7)"+ ":0"
        unsure2 = "Unsure (2)"+ ":0"
        unsure7 = "Unsure (7)"+ ":0"
        notRevel2 = "Not Relevent (2)"+ ":0"
        notRevel7 = "Not Relevent (7)"+ ":0"

        actualentire={}
        actualentire2 = {}
        if (firstOrSecond=="first"):
            productReview = 0
            newsCoverage = 0
            unboxing = 0
            demonstration = 0
            Advertisment = 0
            UnstructredUse = 0
            Unsure = 0
            notRevelant = 0
            if (row['labelId']=="1"):
                productReview = 1
                productReview2 = "Product Review (2)" + ":1"
            elif row['labelId']=="2":
                newsCoverage2 = "News Coverage (2)" + ":1"
            elif (row['labelId']=="3"):
                unboxing = 1
                unboxing2 = "Unboxing (2)"+ ":1"
            elif (row['labelId']=="4"):
                demonstration = 1
                demonstration2 = "Demonstration (2)"+ ":1"
            elif (row['labelId']=="5"):
                Advertisment = 1
                ad2 = "Advertisement (2)"+ ":1"
            elif (row['labelId']=="6"):
                UnstructredUse = 1
                unstruct2 = "Unstructured Use (2)"+ ":1"
            elif (row['labelId']=="7"):
                Unsure = 1
                unsure2 = "Unsure (2)"+ ":1"
            elif (row['labelId']=="8"):
                notRevelant = 1
                notRevel2 = "Not Relevent (2)"+ ":1"
            print productReview2
            #actualentire = {"ElementId": elementId, "Product Review (2)" : productReview, "News Coverage (2)": newsCoverage, "Unboxing (2)": unboxing , "Demonstration (2)" : demonstration, "Advertisement (2)": Advertisment , "Unstructured Use (2)": UnstructredUse , "Unsure (2)": Unsure ,  "Not Relevent (2)": notRevelant }
            firstOrSecond=="second"
        else:
            productReview = 0
            newsCoverage = 0
            unboxing = 0
            demonstration = 0
            Advertisment = 0
            UnstructredUse = 0
            Unsure = 0
            notRevelant = 0
            if (row['labelId']==1):
                productReview = 1
                productReview7 = "Product Review (7)" + ":1"

            elif row['labelId']==2:
                newsCoverage = 1
                newsCoverage7 = "News Coverage (7)" + ":1"
            elif (row['labelId']==3):
                unboxing = 1
                unboxing7 = "Unboxing (7)" + ":1"
            elif (row['labelId']==4):
                demonstration = 1
                demonstration7 = "Demonstration (7)" + ":1"
            elif (row['labelId']==5):
                Advertisment = 1
                ad7 = "Advertisement (7)" + ":1"
            elif (row['labelId']==6):
                UnstructredUse = 1
                unstruct7 = "Unstructured Use (7)" + ":1"
            elif (row['labelId']==7):
                Unsure = 1
                unsure7 = "Unsure (7)" + ":1"
            elif (row['labelId']==8):
                notRevelant = 1
                notRevel7 = "Not Relevent (7)" + ":1"
            firstOrSecond="first"
            elementId = elementId+1
            actualentire = {"ElementId": elementId, "Product Review (2)" : productReview, "News Coverage (7)": newsCoverage, "Unboxing (7)": unboxing , "Demonstration (7)" : demonstration, "Advertisement (7)": Advertisment , "Unstructured Use (7)": UnstructredUse , "Unsure (7)": Unsure ,  "Not Relevent (7)": notRevelant }
    # a.append(actualentire)
        outfile.write(json.dumps(actualentire) + "\n")
