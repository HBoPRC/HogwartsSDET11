import requests

from test_requests.test_department.api.wework import WeWork


class Department:
    secret = 'U4nUz683NpltcQYL7LLWv2EfSEux7VXftivbnO1pIHY'

    def get(self, id):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        r = requests.get(url,
                         params={
                             'access_token': WeWork.get_token(self.secret),
                             'id': id
                         })
        return r.json()

    def create(self, name, parentid, **kwargs):
        json = {'name': name, 'parentid': parentid}
        json.update(kwargs)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        r = requests.post(url,
                          params={
                              'access_token': WeWork.get_token(self.secret)
                          },
                          json=json)
        return r.json()

    def update(self, id, **kwargs):
        json = {'id': id}
        json.update(kwargs)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
        r = requests.post(url,
                          params={
                              'access_token': WeWork.get_token(self.secret)
                          },
                          json=json)
        return r.json()

    def delete(self, id):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        r = requests.get(url,
                         params={
                             'access_token': WeWork.get_token(self.secret),
                             'id': id
                         })
        return r.json()
