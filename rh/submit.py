import requests
import json
import re

initUrl = 'http://senbatsu.akb48-china.com/f/VlsoJN'
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
    'Referer': 'http://senbatsu.akb48-china.com/f/VlsoJN',
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
           value=''):
    global cookies
    global csrf
    url = 'http://senbatsu.akb48-china.com/graphql/f/VlsoJN'
    payload = {
        "operationName": "CreatePublishedFormEntry",
        "variables": {
            "input": {
                "formId": "VlsoJN",
                "entryAttributes": {
                    "field_11": nickname,
                    "field_26": {
                        "level_1": "8H3c",
                        "level_2": "1568"
                    },
                    "field_28": {
                        "_Kkx": {
                            "field_1": ["b6iD"]
                        },
                        "OTOl": {
                            "field_1": ["2RqI"]
                        },
                        "11oS": {
                            "field_1": ["Z4dr"]
                        },
                        "34M0": {
                            "field_1": ["qTq5"]
                        },
                        "Y_Aw": {
                            "field_1": []
                        },
                        "vbJZ": {
                            "field_1": []
                        },
                        "juB5": {
                            "field_1": []
                        }
                    },
                    "field_18": meetingList,
                    "field_17": location,
                    "field_30": value,
                    "field_25": "Crzt"
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
                "fillingDuration": 297
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
