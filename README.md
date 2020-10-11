# AKB48TeamSHTools
总选投票券自动识别 + 投票脚本(开发中) + rh（待开发）

- [x] 腾讯云OCR识别投票码

- [x] 官网接口验证投票码有效性

- [x] 全csv（excel打开）输出

- [] 自动投票（待验证）


## 目录结构

```
.
├── LICENSE
├── README.md
├── output.csv // 默认输出文件（w+）
├── resources // 此文件夹放投票券图片
│   ├── xxx.JPG
│   └── xxx.JPG
└── senbatsu // 此文件夹为总选脚本相关
    ├── main.py // 主入口
    ├── ocr.py // 腾讯云ocr
    ├── submit.py // 投票脚本（未验证）
    └── validate.py // 检验投票码有效性
```

## 依赖

腾讯云OCR([doc](https://cloud.tencent.com/document/product/866/33526)): [生成地址](https://console.cloud.tencent.com/cam/capi)
 - SecretId
 - SecretKey

Python3
 - [腾讯云SDK](https://github.com/TencentCloud/tencentcloud-sdk-python): `pip3 install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python`
 - requests: `pip3 install requests`

## 总选投票使用简介

1. 拍照片，全部放在`resources`文件夹下，一定为JPG格式,不然自己去改`senbatsu/ocr.py`[第20行](https://github.com/chinshin/AKB48TeamSHTools/blob/main/senbatsu/ocr.py#L20);

样张(务必要把官方网站和投票地址两行拍进去)：![image](https://user-images.githubusercontent.com/14086338/95672256-ef8d0900-0bd1-11eb-92aa-7eee813a0633.png)

2. 配置腾讯云环境变量;
```
export TENCENTCLOUD_SECRET_ID=你的SecretId
export TENCENTCLOUD_SECRET_KEY=你的SecretKey
```

3. 运行 `python3 senbatsu/main.py`,屏幕上会有类似输出如下

```
$ python3 senbatsu/main.py 
总图片数:  2
key  ag**********80  有效, value =  5f**********f0
key  0q**********30  无效
```

请仔细看一下这里的总图片数，是否与真实图片数一致。

已知问题为：o容易误识别为0。

output.csv 输出类似如下

||||
| - | - | - |
| IMG_0123.JPG | ag**********80 | 5f**********f0 |
| IMG_0119.JPG | 0q**********30 | False |

自动投票功能还在调试，稍后上线。

**注意:** `main.py` [Line 22](https://github.com/chinshin/AKB48TeamSHTools/blob/main/senbatsu/main.py#L22) 写死了当前投票的默认值，要测试的人记得改一下，不然我就帮甜甜谢谢你的投票了。

## 已知问题

OCR脚本对小写o与数字0的识别较差
