import time

import requests


class WeWork:
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid = 'wwc002a3c1d514a9d8'
    token = dict()

    @classmethod
    def get_token(cls, secret):
        # 如果对应的 token 已经存在，就不重新请求
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            cls.token[secret] = dict()
            cls.token[secret]['token'] = r['access_token']
            cls.token[secret]['time'] = time.time()
        # 如果 token 超时了，也从新获取
        if time.time() - cls.token[secret]['time'] <= 7200:
            r = cls.get_access_token(secret)
            cls.token[secret]['token'] = r['access_token']
            cls.token[secret]['time'] = time.time()
        return cls.token[secret]['token']

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(cls.token_url,
                         params={
                             'corpid': cls.corpid,
                             'corpsecret': secret
                         })
        assert r.json()['errcode'] == 0
        return r.json()
