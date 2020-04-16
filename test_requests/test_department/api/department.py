import requests


class Department:
    def get(self, token, id):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        r = requests.get(url,
                         params={
                             'access_token': token,
                             'id': id
                         })
        return r.json()

    def create(self, token, name, name_en, parentid, order, id):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        r = requests.post(url,
                          params={
                              'access_token': token
                          },
                          json={
                              "name": name,
                              "name_en": name_en,
                              "parentid": parentid,
                              "order": order,
                              "id": id
                          })
        return r.json()

    def update(self, token, id, name, name_en, parentid, order):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
        r = requests.post(url,
                          params={
                              'access_token': token
                          },
                          json={
                              "id": id,
                              "name": name,
                              "name_en": name_en,
                              "parentid": parentid,
                              "order": order
                          })
        return r.json()

    def delete(self, token, id):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        r = requests.get(url,
                         params={
                             'access_token': token,
                             'id': id
                         })
        return r.json()
