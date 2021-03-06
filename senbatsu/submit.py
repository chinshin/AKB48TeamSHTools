import requests
import json
import re

initUrl = 'http://senbatsu.akb48-china.com/f/opf0Si'
initHeader = {
    'Host': 'senbatsu.akb48-china.com',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}
commonHeader = {
    'Host': 'senbatsu.akb48-china.com',
    'Connection': 'keep-alive',
    'accept': '*/*',
    'DNT': '1',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70',
    'content-type': 'application/json;charset=UTF-8',
    'Origin': 'http://senbatsu.akb48-china.com',
    'Referer': 'http://senbatsu.akb48-china.com/f/opf0Si',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}
global cookies
global csrf
cookies = {}
csrf = ''


def initReq():
    global cookies
    global csrf
    res = requests.get(initUrl, headers=initHeader)
    cookies = requests.utils.dict_from_cookiejar(res.cookies)
    # cookie = "; ".join([str(x)+"="+str(y) for x,y in cookies.items()])
    csrf = re.findall('<meta name="csrf-token" content="(.*?)"', res.text,
                      re.S)[0]
    cookies['csrf_token'] = csrf


def submit(nickname='测试',
           location='上海市',
           meetingList=['qaMu'],
           value='',
           member='kQmz'):
    global cookies
    global csrf
    url = 'http://senbatsu.akb48-china.com/graphql/f/opf0Si'
    payload = {
        "operationName": "CreatePublishedFormEntry",
        "variables": {
            "input": {
                "formId": "opf0Si",
                "entryAttributes": {
                    "field_11": nickname,
                    "field_18": meetingList,
                    "field_17": location,
                    "field_25": value,
                    "field_27": member
                },
                "captchaData": None,
                "weixinAccessToken": None,
                "xFieldWeixinOpenid": None,
                "weixinInfo": None,
                "prefilledParams": "",
                "embedded": False,
                "backgroundImage": False,
                "formMargin": False,
                "hasPreferential": False,
                "fillingDuration": 95
            }
        },
        "extensions": {
            "persistedQuery": {
                "version":
                1,
                "sha256Hash":
                "4cd6a9aef2820b2c3215f6ddfa87093869461f76f3f2016738f4307268a7df98"
            }
        }
    }
    header = commonHeader
    header['X-CSRF-TOKEN'] = csrf
    header['Cookie'] = "; ".join([str(x)+"="+str(y) for x,y in cookies.items()])
    res = requests.post(url, headers=header, data=json.dumps(payload))
    newCookies = requests.utils.dict_from_cookiejar(res.cookies)
    cookies['_gd_session'] = newCookies['_gd_session']
    if res.status_code == 200:
        return res
    else:
        return False


initReq()
