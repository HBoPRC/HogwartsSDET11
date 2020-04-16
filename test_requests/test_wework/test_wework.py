import requests


class TestWeWork:
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid = 'wwc002a3c1d514a9d8'
    secret = 'dIsTlncgbbJ1V95H6woafAPdE_TFUllYY1UeT_3w154'
    token = ''

    @classmethod
    def setup_class(cls):
        r = requests.get(cls.token_url,
                         params={
                             'corpid': cls.corpid,
                             'corpsecret': cls.secret
                         })
        assert r.json()['errcode'] == 0
        cls.token = r.json()['access_token']

    def test_get_token(self):
        assert self.token is not None
