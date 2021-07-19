import csv
from collections import Counter

with open('SOCR-HeightWeight.csv', newline= '') as f:
    readfile = csv.reader(f)
    file_data = list(readfile)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    weight = file_data [i][2]
    new_data.append(float(weight))

data = Counter(new_data)
modeData = {
    "75-85" : 0,
    "85-95" : 0,
    "95-105" : 0,
    "105-115" : 0,
    "115-125" : 0,
    "125-135" : 0,
    "135-145" : 0,
    "145-155" : 0,
    "155-165" : 0,
    "165-175" : 0,
    
}
for height, occurance in data.items():
    if 75<float(weight)<85:
        modeData["75-85"]+=occurance
    elif 85<float(weight)<95:
        modeData["85-95"]+=occurance
    elif 95<float(weight)<105:
        modeData["95-105"]+=occurance
    elif 105<float(weight)<115:
        modeData["105-115"]+=occurance
    elif 115<float(weight)<125:
        modeData["115-125"]+=occurance
    elif 125<float(weight)<135:
        modeData["125-135"]+=occurance
    elif 135<float(weight)<145:
        modeData["135-145"]+=occurance
    elif 145<float(weight)<155:
        modeData["145-155"]+=occurance
    elif 155<float(weight)<165:
        modeData["155-165"]+=occurance
    elif 165<float(weight)<175:
        modeData["165-175"]+=occurance

    
    
modeRange, modeOccurance = 0,0
for range, occurance in modeData.items():
    if occurance > modeOccurance:
        modeRange, modeOccurance = [int(range.split("-")[0]), int(range.split("-")[1])], occurance
mode = float((modeRange[0] + modeRange[1])/2)
print("Mode is : " + str(mode))
