from pprint import pprint

import requests


def test_request():
    r = requests.get('https://home.testing-studio.com/categories.json')
    pprint(r)
    assert r.status_code == 200


def test_get():
    r = requests.get('https://httpbin.testing-studio.com/get',
                     params={
                         'a': 1,
                         'b': 2
                     })
    print(r)
    assert r.status_code == 200
