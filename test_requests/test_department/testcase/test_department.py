import pytest

from test_requests.test_department.api.department import Department
from test_requests.test_department.api.wework import WeWork


class TestDepartment:
    secret = 'U4nUz683NpltcQYL7LLWv2EfSEux7VXftivbnO1pIHY'

    @classmethod
    def setup_class(cls):
        cls.department = Department()
        cls.token = WeWork.get_token(cls.secret)

    def test_get_token(self):
        r = WeWork.get_access_token(self.secret)
        assert r['errcode'] == 0

    @pytest.mark.parametrize('name, name_en, parentid, order, id', [
        ('广州研发中心', 'RDGZ', 1, 1, 2),
        ('广州研发中心子部门1', 'RDGZ', 2, 1, 3),
        ('广州研发中心子部门2', 'RDGZ', 2, 2, 4),
        ('成都研发中心', 'RDCD', 1, 2, 5)
    ])
    def test_create_department(self, name, name_en, parentid, order, id):
        r = self.department.create(name=name, name_en=name_en, parentid=parentid, order=order, id=id)
        assert r['errcode'] == 0

    def test_get_department(self):
        r = self.department.get(id=0)
        assert r['errcode'] == 0

    @pytest.mark.parametrize('id, name, name_en, parentid, order', [
        (2, '广州研发中心UPDATE', 'RDGZ', 1, 1),
        (3, '广州子部门1顺序', 'RDGZ-2', 2, 2),
        (4, '广州子部门2父级', 'RDGZ-1', 3, 1),
        (5, '成都研发中心', 'RDCDUPDATE', 1, 2)
    ])
    def test_update_department(self, id, name, name_en, parentid, order):
        r = self.department.update(id=2, name='广州研发中心Update', name_en='RDGZ', parentid=1, order=1)
        assert r['errcode'] == 0

    @pytest.mark.parametrize(' id', [2, 5, 100, ])
    def test_delete_department(self, id):
        r = self.department.delete(id=id)
        assert r['errcode'] == 0
