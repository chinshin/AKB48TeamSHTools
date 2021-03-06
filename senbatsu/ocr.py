import base64
import requests
import os
import json
import csv

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models


def isContainChinese(s):
    for c in s:
        if ('\u4e00' <= c <= '\u9fa5'):
            return True
    return False


def ocrFiles():
    try:
        resourceList = []

        for filename in os.listdir(r"./resources"):
            if 'JPG' in filename.upper():
                resourceList.append(filename)
        print("总图片数: ", len(resourceList))

        cred = credential.Credential(os.environ.get("TENCENTCLOUD_SECRET_ID"),
                                    os.environ.get("TENCENTCLOUD_SECRET_KEY"))
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = ocr_client.OcrClient(cred, "ap-shanghai", clientProfile)

        for filename in resourceList:
            postDict = { 'filename': filename, 'ocrStatus': False, 'postKey': '' }
            try:
                with open("./resources/%s" % filename, 'rb') as file:
                    req = models.GeneralEfficientOCRRequest()
                    content = file.read()
                    b64 = str(base64.b64encode(content), 'utf-8')
                    req.ImageBase64 = b64
                    resp = client.GeneralEfficientOCR(req)
                    data = json.loads(resp.to_json_string())
                    # print(resp.to_json_string())
                    for index, value in enumerate(data['TextDetections']):
                        if '投票地址' in value['DetectedText'] or 'senbatsu' in value['DetectedText']:
                            targetItem1 = data['TextDetections'][index + 1]['DetectedText'].replace(' ', '')
                            targetItem2 = data['TextDetections'][index + 2]['DetectedText'].replace(' ', '')
                            if isContainChinese(targetItem1):
                                postDict['postKey'] = targetItem2
                            else:
                                postDict['postKey'] = targetItem1
            except Exception as e:
                pass
            if postDict['postKey']:
                postDict['ocrStatus'] = True
            print(postDict)
            yield(postDict)

    except TencentCloudSDKException as err:
        print(err)


def output():
    with open('ocr_output.csv', 'w+') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(["文件名", "券码"])
        for i in ocrFiles():
            csvWriter.writerow([i['filename'], i['postKey']])
