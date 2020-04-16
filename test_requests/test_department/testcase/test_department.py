import json

import requests

from test_requests.test_department.api.department import Department


class TestDepartment:
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid = 'wwc002a3c1d514a9d8'
    secret = 'U4nUz683NpltcQYL7LLWv2EfSEux7VXftivbnO1pIHY'
    token = ''

    @classmethod
    def setup_class(cls):
        r = requests.get(cls.token_url,
                         params={
                             'corpid': cls.corpid,
                             'corpsecret': cls.secret
                         })
        cls.token = r.json()['access_token']
        cls.department = Department()

    # todo:PO
    def test_create_department(self):
        r = self.department.create(token=self.token, name='广州研发中心', name_en='RDGZ', parentid=1, order=1, id=2)
        print(json.dumps(r, indent=4))
        assert r['errcode'] == 0

    # todo:PO
    def test_get_department(self):
        r = self.department.get(token=self.token, id=0)
        print(json.dumps(r, indent=4))
        assert r['errcode'] == 0

    # todo:PO
    def test_update_department(self):
        r = self.department.update(token=self.token, id=2, name='广州研发中心Update', name_en='RDGZ', parentid=1, order=1)
        print(json.dumps(r, indent=4))
        assert r['errcode'] == 0

    # todo:PO
    def test_delete_department(self):
        r = self.department.delete(token=self.token, id=2)
        print(json.dumps(r, indent=4))
        assert r['errcode'] == 0
