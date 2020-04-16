import json

import requests


class TestDepartment:
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid = 'wwc002a3c1d514a9d8'
    secret = 'U4nUz683NpltcQYL7LLWv2EfSEux7VXftivbnO1pIHY'
    access_token = ''

    @classmethod
    def setup_class(cls):
        r = requests.get(cls.token_url,
                         params={
                             'corpid': cls.corpid,
                             'corpsecret': cls.secret
                         })
        cls.access_token = r.json()['access_token']

    # todo:PO
    def test_create_department(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        r = requests.post(url,
                          params={
                              'access_token': self.access_token
                          },
                          json={
                              "name": "广州研发中心",
                              "name_en": "RDGZ",
                              "parentid": 1,
                              "order": 1,
                              "id": 2
                          })
        print(json.dumps(r.json(), indent=4))
        print(r.json()['errmsg'])
        assert r.json()['errcode'] == 0

    # todo:PO
    def test_get_department(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        r = requests.get(url,
                         params={
                             'access_token': self.access_token,
                             'id': 0
                         })
        print(json.dumps(r.json(), indent=4))
        print(r.json()['errmsg'])
        for d in r.json()['department']:
            print(d['name'])
        assert r.json()['errcode'] == 0

    # todo:PO
    def test_update_department(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
        r = requests.post(url,
                          params={
                              'access_token': self.access_token
                          },
                          json={
                              "id": 2,
                              "name": "广州研发中心Update",
                              "name_en": "RDGZ",
                              "parentid": 1,
                              "order": 1
                          })
        print(json.dumps(r.json(), indent=4))
        print(r.json()['errmsg'])

    # todo:PO
    def test_delete_department(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        r = requests.get(url,
                         params={
                             'access_token': self.access_token,
                             'id': 2
                         })
        print(json.dumps(r.json(), indent=4))
        print(r.json()['errmsg'])
        assert r.json()['errcode'] == 0
