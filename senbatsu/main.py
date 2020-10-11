from ocr import ocrFiles
from validate import validateByKey
from submit import submit
import csv

print("====== 开始 ======")
files = ocrFiles()
data = []
print("====== Step 1/3: 识别+验证投票图片 ======")
for file in files:
    postKey = file['postKey']
    file['postValue'] = validateByKey(postKey)
    data.append(file)
print("====== Step 2/3: 输出csv ======")
with open('output.csv', 'w+') as csvFile:
    csvWriter = csv.writer(csvFile)
    for i in data:
        csvWriter.writerow([i['filename'], i['postKey'], i['postValue']])
# print("====== Step 3/3: 自动投票 ======")
# for i in data:
#     if i['postValue']:
#         status = submit(nickname='你的昵称写这里',
#             location='上海市',
#             meetingList=['qaMu'],
#             value=i['postValue'],
#             member='kQmz')
#         if status:
#             print("投票成功", i['filename'], i['postKey'], i['postValue'])
#         else:
#             print("投票失败", i['filename'], i['postKey'], i['postValue'])
print("====== 结束 ======")
