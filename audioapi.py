#!/usr/bin/env python
# -*- coding:utf-8 -*-
# encoding:utf-8
# 调用百度API实现语音合成功能
import json
from urllib import request,parse

def get_token():
    API_Key = "oRwMlx1PqEeN1oV9NxAylzq1"            # 官网获取的API_Key
    Secret_Key = "TSc1CbDlDGX7mNtVoROhaWGH2vPlkwju" # 为官网获取的Secret_Key
    #拼接得到Url
    Url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="+API_Key+"&client_secret="+Secret_Key
    try:
        resp = request.urlopen(Url)
        result = json.loads(resp.read().decode('utf-8'))
        # 打印access_token
        print("access_token:",result['access_token'])
        return result['access_token']
    except request.URLError as err:
        print('token http response http code : ' + str(err.code))

def audioplay():
    # 1、获取 access_token
    token = get_token()
    # 2、将需要合成的文字做2次urlencode编码
    with open("export.txt",encoding = "utf-8") as f:
        content=f.read().splitlines()
        #print(content)
        p=content.index('文本内容:')
    list_without_head=content[p+1:-1]
    content_str=''.join(list_without_head)
    TEXT = content_str
    #print(type(TEXT))
    tex = parse.quote_plus(TEXT)  # 两次urlencode
    #print(tex)
    # 3、设置文本以及其他参数
    params = {'tok': token,     # 开放平台获取到的开发者access_token
              'tex': tex,       # 合成的文本，使用UTF-8编码。小于2048个中文字或者英文数字
              'per': 1,         # 发音人选择, 基础音库：0为度小美，1为度小宇，3为度逍遥，4为度丫丫，
              'spd': 5,         # 语速，取值0-15，默认为5中语速
              'pit': 5,         # 音调，取值0-15，默认为5中语调
              'vol': 5,         # 音量，取值0-15，默认为5中音量
              'aue': 6,         # 下载的文件格式, 3为mp3格式(默认); 4为pcm-16k; 5为pcm-8k; 6为wav（内容同pcm-16k）
              'cuid': "7749py", # 用户唯一标识
              'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数
    # 4、将参数编码，然后放入body，生成Request对象
    data = parse.urlencode(params)
    req = request.Request("http://tsn.baidu.com/text2audio", data.encode('utf-8'))
    # 5、发送post请求
    f = request.urlopen(req)
    result_str = f.read()
    # 6、将返回的header信息取出并生成一个字典
    headers = dict((name.lower(), value) for name, value in f.headers.items())
    # 7、如果返回的header里有”Content-Type: audio/wav“信息，则合成成功
    if "audio/wav" in headers['content-type'] :
        print("tts success")
        # 合成成功即将数据存入文件
        with open("sound/result.wav", 'wb') as of:
            of.write(result_str)

def audioplay_nobook(str):
    token = get_token()
    TEXT = str
    # print(type(TEXT))
    tex = parse.quote_plus(TEXT)  # 两次urlencode
    # print(tex)
    # 3、设置文本以及其他参数
    params = {'tok': token,  # 开放平台获取到的开发者access_token
              'tex': tex,  # 合成的文本，使用UTF-8编码。小于2048个中文字或者英文数字
              'per': 0,  # 发音人选择, 基础音库：0为度小美，1为度小宇，3为度逍遥，4为度丫丫，
              'spd': 5,  # 语速，取值0-15，默认为5中语速
              'pit': 5,  # 音调，取值0-15，默认为5中语调
              'vol': 5,  # 音量，取值0-15，默认为5中音量
              'aue': 6,  # 下载的文件格式, 3为mp3格式(默认); 4为pcm-16k; 5为pcm-8k; 6为wav（内容同pcm-16k）
              'cuid': "7749py",  # 用户唯一标识
              'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数
    # 4、将参数编码，然后放入body，生成Request对象
    data = parse.urlencode(params)
    req = request.Request("http://tsn.baidu.com/text2audio", data.encode('utf-8'))
    # 5、发送post请求
    f = request.urlopen(req)
    result_str = f.read()
    # 6、将返回的header信息取出并生成一个字典
    headers = dict((name.lower(), value) for name, value in f.headers.items())
    # 7、如果返回的header里有”Content-Type: audio/wav“信息，则合成成功
    if "audio/wav" in headers['content-type']:
        print("tts success")
        # 合成成功即将数据存入文件
        with open("sound/result.wav", 'wb') as of:
            of.write(result_str)
