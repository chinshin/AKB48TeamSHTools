from ocr import ocrFiles
from validate import validateByKey
import csv

files = ocrFiles()
data = []
for file in files:
    postKey = file['postKey']
    file['postValue'] = validateByKey(postKey)
    data.append(file)
with open('output.csv', 'w+') as csvFile:
    csvWriter = csv.writer(csvFile)
    for i in data:
        csvWriter.writerow([i['filename'], i['postKey'], i['postValue']])
