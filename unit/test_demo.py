import unittest


class TestDemo(unittest.TestCase):

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')


    def test_sum(self):
        x = 1 + 2
        print(x)
        # 期望值在前面
        self.assertEqual(4, x, f'x={x} exception=3')


if __name__ == '__main__':
    unittest.main()
